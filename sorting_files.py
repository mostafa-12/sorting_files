import os
import shutil
from tkinter import messagebox
#sort files by extensions
def run(file_into=os.getcwd(),output_path=os.getcwd()):
    path=file_into
    os.chdir(path)
    for file in os.listdir(path):
        if file.endswith((".mp3",".acc",".wav",".flac",".m4a")):
            if "music" in os.listdir(output_path):
                shutil.copy(file,f"{output_path}/music")
                os.remove(file)
                print("done : ",file)
                continue
            elif "music" not in os.listdir(output_path) :
                os.mkdir(f"{output_path}/music")
                shutil.copy(file,f"{output_path}/music")
                os.remove(file)
                print("done : ",file)
                continue
            #music files
        if file.endswith(("mp4",".mkv",".mov",".wmv","avi")):
            if "video" in os.listdir(output_path):
                shutil.copy(file,f"{output_path}/video")
                os.remove(file)
                print("done : ",file)
                continue
            elif "video" not in os.listdir(output_path):
                os.mkdir(f"{output_path}/video")
                shutil.copy(file,f"{output_path}/video")
                os.remove(file)
                print("done : ",file)
                continue
            #video files
        if file.endswith((".jpeg",".jpg",".png",".gif",".tiff")):
            if "photo" in os.listdir(output_path):
                shutil.copy(file,f"{output_path}/photo")
                os.remove(file)
                print("done : ",file)
                continue
            elif "photo" not in os.listdir(output_path):
                os.mkdir(f"{output_path}/photo")
                shutil.copy(file,f"{output_path}/photo")
                os.remove(file)
                print("done : ",file)
                continue
            #photo files
        if file.endswith((".pdf",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".txt",".odt")):
            if "documents" in os.listdir(output_path):
                shutil.copy(file,f"{output_path}/documents")
                os.remove(file)
                print("done : ",file)
                continue
            elif "documents" not in os.listdir(output_path):
                os.mkdir(f"{output_path}/documents")
                shutil.copy(file,f"{output_path}/documents")
                os.remove(file)
                print("done : ",file)
                continue
            #documents file
    messagebox.showinfo("alert","working is done")
    # status_bar.config(text=f"status bar : working is done")