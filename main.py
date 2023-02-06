import os
import shutil
path=os.path.dirname(os.path.realpath(__file__))
Files=os.listdir(path)

#sort files by extensions
for file in Files:
    if file.endswith((".mp3",".acc",".wav",".flac",".m4a")):
        if "music" in Files:
            shutil.copy(file,"music")
            os.remove(file)
        else:
            os.mkdir("music")
            shutil.copy(file,"music")
            os.remove(file)
        #music files
    if file.endswith(("mp4",".mkv",".mov",".wmv","avi")):
        pass
        #video files
    if file.endswith((".jpeg",".jpg",".png",".gif",".tiff")):
        pass
        #photo files
    if file.endswith((".pdf",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".txt",".odt")):
        pass
        #documents file