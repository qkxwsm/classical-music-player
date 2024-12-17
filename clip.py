from moviepy.video.io.VideoFileClip import VideoFileClip

# Define the input file and cutoff points
input_file = "file.mp4"
cutoff_points = ["0:00", "1:00"]

# Convert cutoff points to seconds
def time_to_seconds(time_str):
    parts = list(map(int, time_str.split(":")))
    return parts[0] * 60 + parts[1]

cutoff_seconds = [time_to_seconds(t) for t in cutoff_points]

# Process the video file
video = VideoFileClip(input_file)

# Loop through cutoff points to create segments
for i in range(len(cutoff_seconds) - 1):
    start_time = cutoff_seconds[i]
    end_time = cutoff_seconds[i + 1]
    segment = video.subclip(start_time, end_time)
    output_file = f"clip_{i+1}.mp4"
    segment.write_videofile(output_file, codec="libx264", audio_codec="aac")

print("Clipping completed!")
