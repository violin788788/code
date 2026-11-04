import subprocess

input_file = "input.mp4"
output_file = "output_rotated.mp4"

subprocess.run([
    "ffmpeg",
    "-i", input_file,
    "-vf", "transpose=2",
    "-c:a", "copy",
    output_file
], check=True)


"""

What transpose values mean
transpose=0 → 90° counter-clockwise + vertical flip
transpose=1 → 90° clockwise
transpose=2 → 90° counter-clockwise
transpose=3 → 90° clockwise + vertical flip

"""