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


