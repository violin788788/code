

import subprocess

def mp4_to_mp3(mp4_file, mp3_file):
    command = [
        "ffmpeg",
        "-i", mp4_file,
        "-q:a", "0",
        "-map", "a",
        mp3_file
    ]
    subprocess.run(command)

# Example usage
mp4_to_mp3("convert.mp4", "convert.mp3")