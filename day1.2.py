import os
import shutil

cwd = os.getcwd()

#create folder
os.makedirs("media_files", exist_ok=True)
folder_path = "media_files"

#create 9 sample files
files = ['photo1.jpg','photo2.png', 'image.gif', 'video1.mp4', 'video2.avi', 'clip.mov', 'doc1.pdf', 'doc2.docx', 'notes.txt']
for file in files:
    file_path = os.path.join(folder_path, file)
    with open(file_path, 'w') as wr:
        wr.write(f'Sample Content for {file}')

#create 3 new folders in root dir
os.makedirs('images', exist_ok=True)
images_folder = "images"
os.makedirs('videos', exist_ok=True)
videos_folder = "videos"
os.makedirs('docs', exist_ok=True)
docs_folder = "docs"

#move files based on type
file_list = os.listdir(folder_path)
for file in file_list:
    if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.gif'):
        shutil.move(os.path.join(folder_path, file), images_folder)
    elif file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.mov'):
        shutil.move(os.path.join(folder_path, file), videos_folder)
    elif file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.txt'):
        shutil.move(os.path.join(folder_path, file), docs_folder)
print('Files have been moved')

print(os.listdir(images_folder))
print(os.listdir(videos_folder))
print(os.listdir(docs_folder))
