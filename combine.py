# from moviepy.editor import VideoFileClip, concatenate_videoclips

# clip1 = VideoFileClip("file1.mp4")
# clip2 = VideoFileClip("file2.mp4")

# combined = concatenate_videoclips([clip1, clip2])

# combined.write_videofile("file.mp4", codec="libx264", audio_codec="aac")

import subprocess, os

input_files = ['file1.mp4', 'file2.mp4']

input_list = '\n'.join(f"file '{f}'" for f in input_files)

with open('inputs.txt', 'w') as f:
    f.write(input_list)

subprocess.run([
    'ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'inputs.txt',
    '-c', 'copy', 'output.mp4'
])

os.remove('inputs.txt')