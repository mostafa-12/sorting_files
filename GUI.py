import tkinter
from tkinter import ttk ,messagebox
from PIL import ImageTk,Image
import pyautogui
import os
#screen size
Screen_width=pyautogui.size()[0]
Screen_height=pyautogui.size()[1]
#main wind
root=tkinter.Tk()
root.geometry(f"370x400+{int(Screen_width/3)}+{int(Screen_height/5)}")
root.configure(bg="white")
root.iconbitmap("C:/Users/ELPRO/Documents/bitbucket/sorting_by_python/Logos/logo.ico")
root.resizable(0,0)
#logo
myimage=ImageTk.PhotoImage(Image.open("C:/Users/ELPRO/Documents/bitbucket/sorting_by_python/Logos/logo.jpg"))
#Entries
path=tkinter.Entry(root,width=30,bd=3,relief="ridge")
path.place(relx=.27,rely=.55)

sort_in=tkinter.Entry(root,width=30,bd=3,relief="ridge")
sort_in.place(relx=.27,rely=.65)
#Labels

path_lbl=tkinter.Label(root,text="Path : ", font=("Arial Rounded MT Bold",10),bg="white")

path_lbl.place(rely=.55,relx=.1)

Sort_in_lbl=tkinter.Label(root,text="sort in : ", font=("Arial Rounded MT Bold",10),bg="white")

Sort_in_lbl.place(rely=.65,relx=.1)

img=tkinter.Label(root,image=myimage,bd=0,relief="flat")
img.place(rely=.001,relx=.099)


#Buttons
browes_path_btn=tkinter.Button(root,text="Browes",bg="white")
browes_path_btn.place(rely=.55,relx=.8)

browes_SORTin_btn=tkinter.Button(root,text="Browes",bg="white")
browes_SORTin_btn.place(rely=.65,relx=.8)

submit_btn=tkinter.Button(root,text="Submit",width=12,height=2)
submit_btn.place(rely=.80,relx=.4)

root.mainloop()




