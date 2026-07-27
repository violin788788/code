import subprocess
import json

def get_video_info(file_path):
    cmd = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format:stream",
        "-print_format", "json",
        file_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

files = [
            "deb.mp4"
        ]

for f in files:
    print(f"\n=== {f} ===")
    info = get_video_info(f)
    for stream in info["streams"]:
        codec_type = stream.get("codec_type")
        codec_name = stream.get("codec_name")
        if codec_type and codec_name:
            print(f"{codec_type.capitalize()} Codec: {codec_name}")
