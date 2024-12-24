from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load video files
clip1 = VideoFileClip("clip_1.mp4")
clip2 = VideoFileClip("clip_3.mp4")

# Combine back-to-back
combined = concatenate_videoclips([clip1, clip2])

# Export the result
combined.write_videofile("clip.mp4", codec="libx264", audio_codec="aac")