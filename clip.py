from moviepy.video.io.VideoFileClip import AudioFileClip, VideoFileClip

input_file = "file.mp4"
cutoff_points = ["0:00", "14:10", "27:44", "34:14"]

# Convert cutoff points to seconds
def time_to_seconds(time_str):
    parts = list(map(int, time_str.split(":")))
    return parts[0] * 60 + parts[1]

cutoff_seconds = [time_to_seconds(t) for t in cutoff_points]

# Try loading the video, fall back to audio if needed
try:
    media = VideoFileClip(input_file)
except Exception:
    media = AudioFileClip(input_file)

# Loop through cutoff points to create segments
for i in range(len(cutoff_seconds) - 1):
    start_time = cutoff_seconds[i]
    end_time = cutoff_seconds[i + 1]
    segment = media.subclip(start_time, end_time)
    output_file = f"clip_{i+1}.mp4"

    # Remove video if present, keep only audio
    if hasattr(segment, "audio") and segment.audio is not None:
        audio_only = segment.audio
        audio_only.write_audiofile(output_file, codec="aac")
    else:
        segment.write_audiofile(output_file, codec="aac")

print("Audio clipping completed!")
