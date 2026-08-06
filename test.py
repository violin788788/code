import subprocess
import sys
def run(cmd):
    print("Running:",cmd)
    subprocess.check_call(cmd)
def main():
    run([sys.executable,"-m","pip","install","--upgrade","pip","setuptools","wheel"])
    run([sys.executable,"-m","pip","install","torch==1.13.1","torchaudio==0.13.1"])
    run([sys.executable,"-m","pip","install","numpy==1.21.6"])
    run([sys.executable,"-m","pip","install","numba==0.53.1"])
    run([sys.executable,"-m","pip","install","librosa==0.9.2"])
    run([sys.executable,"-m","pip","install","TTS==0.13.3"])
    print("Done!")
if __name__=="__main__":
    main()