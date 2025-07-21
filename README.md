Python File Organizer Lab

This Python script demonstrates how to organize media files using basic file and directory operations. It uses the `os` and `shutil` modules to move files into folders based on their type — images, videos, or documents.

## Features

1. Creates a folder named `media_files`  
   This directory acts as the source containing various file types.

2. Generates sample files 
   The following files are created with sample content:
   - Images: `photo1.jpg`, `photo2.png`, `image.gif`
   - Videos: `video1.mp4`, `video2.avi`, `clip.mov`
   - Documents: `doc1.pdf`, `doc2.docx`, `notes.txt`

3. Creates organized folders  
   Three folders are created in the root directory:
   - `images/` for image files
   - `videos/` for video files
   - `docs/` for document files

5. Moves files based on extension
   - `.jpg`, `.png`, `.gif` → `images/`
   - `.mp4`, `.avi`, `.mov` → `videos/`
   - `.pdf`, `.docx`, `.txt` → `docs/`

6. Displays the final state of folders
   - Lists the content of each destination folder after the files have been moved.

##Sample Output

```bash
Files have been moved
['photo1.jpg', 'photo2.png', 'image.gif']
['video1.mp4', 'video2.avi', 'clip.mov']
['doc1.pdf', 'doc2.docx', 'notes.txt']
