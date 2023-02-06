import os
import shutil
path=os.path.dirname(os.path.realpath(__file__))


#sort files by extensions
for file in os.listdir(path):
    if file.endswith((".mp3",".acc",".wav",".flac",".m4a")):
        if "music" in os.listdir(path):
            shutil.copy(file,"music")
            os.remove(file)
            print("done : ",file)
            continue
        elif "music" not in os.listdir(path) :
            os.mkdir("music")
            shutil.copy(file,"music")
            os.remove(file)
            print("done : ",file)
            continue
        #music files
    if file.endswith(("mp4",".mkv",".mov",".wmv","avi")):
        if "video" in os.listdir(path):
            shutil.copy(file,"video")
            os.remove(file)
            print("done : ",file)
            continue
        elif "video" not in os.listdir(path):
            os.mkdir("video")
            shutil.copy(file,"video")
            os.remove(file)
            print("done : ",file)
            continue
        #video files
    if file.endswith((".jpeg",".jpg",".png",".gif",".tiff")):
        if "photo" in os.listdir(path):
            shutil.copy(file,"photo")
            os.remove(file)
            print("done : ",file)
            continue
        elif "photo" not in os.listdir(path):
            os.mkdir("photo")
            shutil.copy(file,"photo")
            os.remove(file)
            print("done : ",file)
            continue
        #photo files
    if file.endswith((".pdf",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".txt",".odt")):
        if "documents" in os.listdir(path):
            shutil.copy(file,"documents")
            os.remove(file)
            print("done : ",file)
            continue
        elif "documents" not in os.listdir(path):
            os.mkdir("documents")
            shutil.copy(file,"documents")
            os.remove(file)
            print("done : ",file)
            continue
        #documents file