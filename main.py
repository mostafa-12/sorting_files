import os
import shutil
path=os.path.dirname(os.path.realpath(__file__))


#sort files by extensions
for file in os.listdir(path):
    if file.endswith((".mp3",".acc",".wav",".flac",".m4a")):
        if "music" in os.listdir(path):
            shutil.copy(file,"music")
            os.remove(file)
            print("done")
            continue
        elif "music" not in os.listdir(path) :
            os.mkdir("music")
            shutil.copy(file,"music")
            os.remove(file)
            print("done")
            continue
        #music files
    if file.endswith(("mp4",".mkv",".mov",".wmv","avi")):
        if "video" in os.listdir(path):
            shutil.copy(file,"video")
            os.remove(file)
            print("done")
            continue
        elif "video" not in os.listdir(path):
            os.mkdir("video")
            shutil.copy(file,"video")
            os.remove(file)
            print("done")
            continue
        #video files
    if file.endswith((".jpeg",".jpg",".png",".gif",".tiff")):
        pass
        #photo files
    if file.endswith((".pdf",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".txt",".odt")):
        pass
        #documents file