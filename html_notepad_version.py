from tkinter import*
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import messagebox
import os
import random
import webbrowser

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.title("HTML Editor")

open_img=ImageTk.PhotoImage(Image.open("open_file.png"))
save_img=ImageTk.PhotoImage(Image.open("save_file.png"))
run_img=ImageTk.PhotoImage(Image.open("run.png"))

label_1=Label(root,text="File Name")
label_1.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file=Entry(root)
input_file.place(relx=0.46,rely=0.03,anchor=CENTER)

textbox=Text(root,height=35,width=80)
textbox.place(relx=0.5,rely=0.55,anchor=CENTER)

name=""
def openFile():
    global name
    
    input_file.delete(0,END)
    textbox.delete(1.0,END)
    
    html_file=filedialog.askopenfilename(title="OPEN HTML FILE",filetypes=(("html Files","*.html"),))
    print(html_file)
    
    name=os.path.basename(html_file)
    onlyname=name.split('.')[0]
    
    input_file.insert(END,onlyname)
    root.title(onlyname)
    
    html_file=open(name,'r')
    content=html_file.read()
    textbox.insert(END,content)
    
    html_file.close()
    
    
def saveFile():
    input_name=input_file.get()
    file=open(input_name+".html","w")
    
    data=textbox.get(1.0,END)
    print(data)
    
    file.write(data)
    
    input_file.delete(0,END)
    textbox.delete(1.0,END)
    
    messagebox.showinfo("Update","Success!")
    
    
def runFile():
    global name
    webbrowser.open(name)

    
open_button=Button(root,text="Open File",command=openFile,image=open_img)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

save_button=Button(root,text="Save File",command=saveFile,image=save_img)
save_button.place(relx=0.11,rely=0.03,anchor=CENTER)

run_button=Button(root,text="Run File",command=runFile,image=run_img)
run_button.place(relx=0.17,rely=0.03,anchor=CENTER)

root.mainloop()