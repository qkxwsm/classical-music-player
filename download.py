import os
import shutil

pieces = []

source_base = os.path.expanduser("~/documents/code/music/Music")
destination_folder = os.path.expanduser("~/Downloads/pieces")

os.makedirs(destination_folder, exist_ok=True)

for piece in pieces:
    if piece[4] != 5:
        composer, title = piece[2], piece[0]
        num_copies = piece[8] if len(piece) > 8 else 1
        for i in range(num_copies):
            copy_suffix = f" {i}" if i > 0 else ""
            source_file = os.path.join(source_base, f"{composer} {title}{copy_suffix}.mp4")
            destination_file = os.path.join(destination_folder, f"{composer} {title}{copy_suffix}.mp4")

            if os.path.exists(source_file):
                shutil.copy(source_file, destination_file)
                print(f"Copied: {composer} {title}{copy_suffix}")
            else:
                print(f"File not found: {composer} {title}{copy_suffix}")