const express=require("express");
const multer=require("multer");
const fs=require("fs");
const path=require("path");
const {spawn}=require("child_process");
const crypto=require("crypto");
const os=require("os");
const app=express();
const PORT=5000;
const HOST="127.0.0.1";
const UPLOAD_FOLDER=path.join(__dirname,"uploads");
const OUTPUT_FOLDER=path.join(__dirname,"outputs");
const WORKER=path.join(__dirname,"worker.py");
fs.mkdirSync(UPLOAD_FOLDER,{recursive:true});
fs.mkdirSync(OUTPUT_FOLDER,{recursive:true});
app.set("view engine","ejs");
app.set("views",path.join(__dirname,"views"));
app.use(express.urlencoded({extended:true}));
app.use(express.json());
const upload=multer({
    dest:UPLOAD_FOLDER,
    limits:{
        fileSize:2*1024*1024*1024
    }
});
const jobs=new Map();
function createJobId(){
    return crypto.randomUUID();
}
function startWorker(jobId,videoPath,replacementPath,outputPath){
    const python=process.platform==="win32"?"python":"python3";
    const worker=spawn(python,[WORKER,"--video",videoPath,"--replacement",replacementPath,"--output",outputPath],{
        env:{
            ...process.env,
            OMP_NUM_THREADS:"1",
            ORT_NUM_THREADS:"1"
        }
    });
    jobs.get(jobId).status="Starting...";
    jobs.get(jobId).progress=0;
    worker.stdout.on("data",data=>{
        const text=data.toString();
        console.log(`[${jobId}] ${text.trim()}`);
        const progressMatch=text.match(/PROGRESS:(\d+)/);
        if(progressMatch){
            jobs.get(jobId).progress=Math.min(parseInt(progressMatch[1],10),100);
        }
        const statusMatch=text.match(/STATUS:(.*)/);
        if(statusMatch){
            jobs.get(jobId).status=statusMatch[1].trim();
        }
    });
    worker.stderr.on("data",data=>{
        console.error(`[${jobId}] ${data.toString()}`);
    });
    worker.on("error",err=>{
        console.error(`[${jobId}] Worker error:`,err);
        const job=jobs.get(jobId);
        if(job){
            job.status=err.message;
            job.error=true;
            job.finished=true;
        }
    });
    worker.on("close",code=>{
        const job=jobs.get(jobId);
        if(!job)return;
        if(code===0){
            job.progress=100;
            job.status="Finished.";
            job.finished=true;
            job.error=false;
            job.output=outputPath;
            console.log(`Job ${jobId} finished.`);
        }else{
            job.status=`Worker exited with code ${code}`;
            job.error=true;
            job.finished=true;
        }
    });
}
app.get("/",(req,res)=>{
    res.render("index",{job:null});
});
app.post("/process",upload.fields([{name:"video",maxCount:1},{name:"replacement",maxCount:1}]),(req,res)=>{
    const video=req.files?.video?.[0];
    const replacement=req.files?.replacement?.[0];
    if(!video||!replacement){
        return res.status(400).send("Please select both files.");
    }
    const jobId=createJobId();
    const videoPath=path.join(UPLOAD_FOLDER,`${jobId}_video.mp4`);
    const replacementPath=path.join(UPLOAD_FOLDER,`${jobId}_replacement.png`);
    const outputPath=path.join(OUTPUT_FOLDER,`${jobId}_output.mp4`);
    fs.renameSync(video.path,videoPath);
    fs.renameSync(replacement.path,replacementPath);
    jobs.set(jobId,{
        status:"Starting...",
        progress:0,
        finished:false,
        error:false,
        output:null
    });
    startWorker(jobId,videoPath,replacementPath,outputPath);
    res.redirect(`/status/${jobId}`);
});
app.get("/status/:jobId",(req,res)=>{
    const job=jobs.get(req.params.jobId);
    if(!job){
        return res.status(404).send("Job not found.");
    }
    res.render("index",{
        job,
        jobId:req.params.jobId,
        processing:!job.finished,
        finished:job.finished&&!job.error,
        error:job.error
    });
});
app.get("/api/status/:jobId",(req,res)=>{
    const job=jobs.get(req.params.jobId);
    if(!job){
        return res.status(404).json({error:"Job not found."});
    }
    res.json(job);
});
app.get("/download/:jobId",(req,res)=>{
    const job=jobs.get(req.params.jobId);
    if(!job){
        return res.status(404).send("Job not found.");
    }
    if(!job.finished||job.error){
        return res.status(400).send("Output is not ready.");
    }
    if(!job.output||!fs.existsSync(job.output)){
        return res.status(404).send("Output file not found.");
    }
    res.download(job.output,"output.mp4");
});
app.listen(PORT,HOST,()=>{
    console.log("Face Swap Web App");
    console.log(`Open http://${HOST}:${PORT}`);
    console.log(`OS: ${os.platform()}`);
    if(process.platform==="win32"){
        const {exec}=require("child_process");
        exec(`start http://${HOST}:${PORT}`);
    }
});
