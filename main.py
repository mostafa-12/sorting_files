import tkinter
from tkinter import filedialog
from PIL import ImageTk,Image
import pyautogui
import threading
from sorting_files import run

#screen size
Screen_width=pyautogui.size()[0]
Screen_height=pyautogui.size()[1]
#functions
#bind functions
def clear_path(n):
    if path_var.get() =="insetr path here":
        path_var.set("")

def set_path_var(n):
    if path_var.get()== "":
        path_var.set("insetr path here")

def clear_sort_in(n):
    if sort_in_var.get() =="insert path of output here":
        sort_in_var.set("")

def set_sort_in(n):
    if sort_in_var.get()== "":
        sort_in_var.set("insert path of output here")
############

#set_pathes
def set_path():
    file=filedialog.askdirectory()
    path_var.set(file)
def set_output():
    file=filedialog.askdirectory()
    sort_in_var.set(file)
#######################

# run function
def run0():
    run(path_var.get(),sort_in_var.get())

#main wind
root=tkinter.Tk()
root.geometry(f"370x400+{int(Screen_width/3)}+{int(Screen_height/5)}")
root.configure(bg="white")
root.iconbitmap("Logos/logo.ico")
root.resizable(0,0)
#logo and photos
myimage=ImageTk.PhotoImage(Image.open("Logos/logo.jpg"))
btn_photos=ImageTk.PhotoImage(Image.open("Logos/browse.png"))
#varibales
path_var=tkinter.StringVar()
sort_in_var=tkinter.StringVar()
path_var.set("insetr path here")
sort_in_var.set("insert path of output here")

#Entries
path=tkinter.Entry(root,width=30,bd=0,relief="flat",textvariable=path_var)
path.place(relx=.27,rely=.55)
path.bind("<Enter>",clear_path)
path.bind("<Leave>",set_path_var)
sort_in=tkinter.Entry(root,width=30,bd=0,relief="flat",textvariable=sort_in_var)
sort_in.place(relx=.27,rely=.65)
sort_in.bind("<Enter>",clear_sort_in)
sort_in.bind("<Leave>",set_sort_in)
#Labels

# path_lbl=tkinter.Label(root,text="Path : ", font=("Arial Rounded MT Bold",10),bg="white")

# path_lbl.place(rely=.55,relx=.1)

# Sort_in_lbl=tkinter.Label(root,text="sort in : ", font=("Arial Rounded MT Bold",10),bg="white")

# Sort_in_lbl.place(rely=.65,relx=.1)

img=tkinter.Label(root,image=myimage,bd=0,relief="flat")
img.place(rely=.001,relx=.099)

status_bar=tkinter.Label(root,text="status bar : copyright by white_wolf18",bg="white",fg="#00b7ff",font=("Microsoft JhengHei UI Light",10,"bold"))
status_bar.place(rely=.95,relx=0)
#some beautifule things
tkinter.Frame(root,width=185,height=2,bd=0,relief="flat",bg="#00b7ff").place(relx=.27,rely=.6)
tkinter.Frame(root,width=185,height=2,bd=0,relief="flat",bg="#00b7ff").place(relx=.27,rely=.7)

#Buttons
browes_path_btn=tkinter.Button(root,image=btn_photos,width=42,height=18,bd=0
                               ,relief="flat",bg="white",activebackground="#f6ff00",command=set_path)
browes_path_btn.place(rely=.58,relx=.83)

browes_SORTin_btn=tkinter.Button(root,image=btn_photos,width=42,height=18,bd=0
                                 ,relief="flat",bg="white",activebackground="#f6ff00",command=set_output)
browes_SORTin_btn.place(rely=.68,relx=.83)

submit_btn=tkinter.Button(root,text="Submit",width=12,height=2,font=("Microsoft JhengHei UI Light",16,"bold")
                          ,bd=0,relief="flat",fg="#00b7ff",bg="white",activebackground="#f6ff00",command=threading.Thread(target=run0).start)
submit_btn.place(rely=.75,relx=.3)


root.mainloop()




