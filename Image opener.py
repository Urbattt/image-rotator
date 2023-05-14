from tkinter import * 
from PIL import ImageTk, Image 
from tkinter import filedialog 
import os

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)
name = ""
label = Label(root)
label.place(relx=0.5, rely=0.7, anchor = CENTER)
img_path = ""

def openFile():
    global name 
    file=filedialog.askopenfilename(title="Open File", filetypes=[("Files ", "*.jpg;*.gif;*.png;*.jpeg;*.txt")])
    print(file)
    name = os.path.basename(file)
    formated_name = name.split(".")[0]
    root.title(formated_name)
    img_path = file 
    img = ImageTk.PhotoImage(Image.open(img_path))
    print(img)
    label["image"] = img
    file.close()

def Rotate():
    label.rotate(180)

openfilebtn = Button(root, text ="openfile", command = openFile)
openfilebtn.place(relx=0.5, rely = 0.2, anchor = CENTER)
rotate = Button(root, text= "rotate", command = Rotate)
rotate.place(relx=0.5, rely= 0.7, anchor = CENTER)

root.mainloop()