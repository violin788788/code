import subprocess, os
def get_duration(file_path):
    cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    try: return float(res.stdout.strip())
    except: return 0
def mix_audio_fast(main_file, v1, overlay1, v2, overlay2, v3, output_file):
    dur = get_duration(main_file)
    cmd = ['ffmpeg', '-y', '-i', main_file, '-stream_loop', '-1', '-t', str(dur), '-i', overlay1, '-stream_loop', '-1', '-t', str(dur), '-i', overlay2, '-filter_complex', f'[0:a]volume={v1}[a0];[1:a]volume={v2}[a1];[2:a]volume={v3}[a2];[a0][a1][a2]amix=inputs=3:duration=first:dropout_transition=0', '-c:a', 'libmp3lame', '-q:a', '4', output_file]
    subprocess.run(cmd)
folder, dmitri, plane = "jp_morgan", "dmitri.mp3", "plane_sound.mp3"
for i in range(1, 100):
    main_part = os.path.join(folder, f"jp_morgan_part{i}.mp3")
    out_part = os.path.join(folder, f"jp_morgan_part{i}_mixed.mp3")
    if os.path.exists(main_part):
        print(f"\nProcessing part {i}...")
        mix_audio_fast(main_part, 0.7, dmitri, 0.5, plane, 0.3, out_part)
input("\nAll done! Press Enter to exit...")
