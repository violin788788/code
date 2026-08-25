import sys
sys.path.insert(0, r"A:\Users\-\code")
from utils import *
def show(value):
    #show(epub_file)
    for name, val in globals().items():
        if val is value:
            print(f"{name} = {value}")
            return
    print(value)
#new_file = os.path.join(a,b,c)
drive = os.path.splitdrive(os.getcwd())[0]
cwd = os.getcwd()
files = os.listdir(cwd)



from moviepy import VideoFileClip, AudioFileClip
# Load the video and the new mp3 audio
video = VideoFileClip("ww1.mp4")
new_audio = AudioFileClip("clearwater.mp3")
# Attach the new audio to the video
final_video = video.with_audio(new_audio)
# Write the final result to a new file
final_video.write_videofile("output.mp4", codec="libx264", audio_codec="aac")
# Close clips to free up memory
video.close()
new_audio.close()
final_video.close()

"""
```

<FollowUp>
If you want, let me know:
* Do you need to **adjust the volume** of the new MP3?
* Should the audio **fade in or out**?

I can update the code to handle those edits for you.
</FollowUp>
""" 