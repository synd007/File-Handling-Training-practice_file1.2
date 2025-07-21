import os
import shutil

#create folder
os.makedirs("media_files", exist_ok=True)
folder_path = "media_files"

#create 9 sample files
file = ['photo1.jpg','photo2.png', 'image.gif', 'video1.mp4', 'video2.avi', 'clip.mov', 'doc1.pdf', 'doc2.docx', 'notes.txt']
for file in file:
    with open(file, 'w') as wr:
        wr.write(f'Sample Content for {file}')

#create 3 new folders in root dir
os.makedirs('images', exist_ok=True)
images_folder = "images"
os.makedirs('videos', exist_ok=True)
videos_folder = "videos"
os.makedirs('docs', exist_ok=True)
docs_folder = "docs"

