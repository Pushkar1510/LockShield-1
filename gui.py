from fileinput import filename
from tkinter import*
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb 
from randimage import get_random_image, show_array
from tkinter import messagebox
import matplotlib as mp


root=Tk()
root.title("Lockshield - Hide a Secret Text Message in an Image")
root.geometry ("1280x676")
root.resizable(False, False)
root.configure(bg="#2f4155")


def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetype=(("PNG file","*.png"),("JPG file","*.jpg"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage (img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

def Hide():
    messagebox.showinfo("Info","The data has been successfully hidden")
    global secret
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename),message)

def generate():
    img_size = (250,250)
    imgarr = get_random_image(img_size)
    mp.image.imsave("randimage.png", imgarr)
    img=Image.open("randimage.png")
    img=ImageTk.PhotoImage(img)
    showimage()

def upload_file():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetype=(("PNG file",".png"),("JPG file",".jpg"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=400,height=350)
    lbl.image=img

def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)



def save_png():
    messagebox.showinfo("Info","The image has been saved")
    secret.save("Generated_Image.png")

def save_jpeg():
    messagebox.showinfo("Info","The image has been saved")
    secret.save("Generated_Image.jpeg")

def save_jpg():
    messagebox.showinfo("Info","The image has been saved")
    secret.save("Generated_Image.jpg")


#icon
image_icon=PhotoImage(file="images/gear.png")
root. iconphoto(False,image_icon) 

#logo
logo=PhotoImage()
Label(root, image=logo, bg="black").place(x=10, y=0)
Label(root,text="LOCKSHIELD", bg="#2d4155",fg="#3ddac3",font="arial 25 bold"). place(x=575, y=40)

#first Frame
f=Frame(root, bd=3,bg="black" ,width=500, height=400, relief=GROOVE)
f.place(x=140-25,y=150-50)

lbl=Label(f, fg="black")
lbl.place(x=40,y=10)

#Second Frame
frame2=Frame (root, bd=3,width=500, height=400, bg="white" ,relief=GROOVE)
frame2.place(x=140+500+25, y=150-50)

text1=Text(frame2,font="Robote 20",bg="white", fg="black", relief=GROOVE,wrap=WORD)
text1.place(x=0, y=0,width=500,height=400)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=480,y=0,height=400)

scrollbar1.configure(command=text1.yview)
text1. configure(yscrollcommand=scrollbar1.set)


#third Frame
frame3=Frame (root, bd=3, bg="#3ddac3" ,width=500, height=100, relief=GROOVE)
frame3.place(x=140-25,y=150+400-50)


Button(frame3,text="Generate Image" ,width=12, height=2,font="arial 12 bold", command=generate).place(x=180, y=30)
Button(frame3,text="Select Image" ,width=12, height=2,font="arial 12 bold", command=upload_file).place(x=20, y=30)
Button(frame3,text="Save .png" ,width=12,height=1,font="arial 12 bold", command=save_png) .place(x=340, y=0)
Button(frame3,text="Save .jpeg" ,width=12,height=1,font="arial 12 bold", command=save_jpeg) .place(x=340, y=30)
Button(frame3,text="Save .jpg" ,width=12,height=1,font="arial 12 bold", command=save_jpg) .place(x=340, y=60)
Label(frame3,text="Picture, Image, Photo File", bg="#2f4155", fg="white").place(x=20,y=5)
       
#fourth Frame
frame4=Frame(root, bd=3, bg="#3ddac3" ,width=500, height=100, relief=GROOVE)
frame4.place(x=140-25+500+25+25, y=150+400-50)

Button(frame4, text="Hide Data",width=10, height=2, font= "arial 12 bold", command=Hide) .place(x=20, y=30)
Button(frame4, text="Show Data",width=10,height=2,font="arial 12 bold", command=Show) .place(x=165, y=30)
Button(frame4, text="Use another way",width=15,height=2,font="arial 12 bold", command=Show) .place(x=315, y=30)
Label(frame4,text="Picture, Image, Photo File",bg="#2f4155", fg="white") .place(x=20,y=5)

root.mainloop()