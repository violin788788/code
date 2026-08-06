import subprocess
import sys

def run(pkg):
    print("Installing:",pkg)
    subprocess.check_call([sys.executable,"-m","pip","install",pkg])

def main():
    run("pip==23.3.2")
    run("setuptools==68.0.0")
    run("wheel==0.41.3")
    run("numpy==1.21.6")
    run("scipy==1.7.3")
    run("safetensors==0.3.3")
    run("transformers==4.30.2")
    run("TTS==0.13.3")

if __name__=="__main__":
    main()