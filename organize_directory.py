import os
import shutil
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": [".pdf", ".rtf", ".txt"],
    "AUDIO": [".m4a", ".m4b", ".mp3"],
    "VIDEOS": [".mov", ".avi", ".mp4"],
    "IMAGES": [".jpg", ".jpeg", ".png"],
    "SCRIPTS": [".py"]
}

parent_dir = input("What directory do you need to organize?\n")

def pick_directory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return "MISC"

def organize_directory():
    for file in os.scandir(parent_dir):
        if file.is_dir():
            continue
        file_name = os.path.basename(file)
        file_path = Path(file)
        file_type = file_path.suffix.lower()
        directory = pick_directory(file_type)
        directory_path = Path(directory)
        path = os.path.join(parent_dir, directory_path)
        final_path = os.path.join(path, file_name)
        if directory_path.is_dir() != True:
            os.mkdir(path)
        shutil.move(file_path, final_path)
        
        
organize_directory()