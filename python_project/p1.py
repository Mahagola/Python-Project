from tkinter import*
from PIL import Image, ImageTk
import random
import os
var = Tk()
var.geometry("480x610")
var.minsize(height=610, width=480)
var.maxsize(height=610, width=480)


def fun(i):
    print(i)

# heading---------------------------------------------------
active = random.choice(["cats", "hydrant", "stairs", "traffic"])

Label(var, text="Select all images with ", font=('verdana', 23)).pack(
    side=TOP, pady=4, padx=15, anchor='w')
Label(var, text=f"{active}".upper(), font=('verdana', 24, 'bold')).pack(
    side=TOP, pady=3, padx=20, anchor='nw')

# verify image button----------------------------------------

photo = PhotoImage(file=r"check.png")
button = Button(var, image=photo, compound=RIGHT,
                borderwidth=0, command=var.destroy)
button.place(rely=1, relx=0.98, x=0, y=0, anchor=SE)

# reload button----------------------------------------------

photo2 = PhotoImage(file=r"reload.png")
button2 = Button(var, image=photo2, compound=RIGHT,
                 borderwidth=0, command=var.destroy)
button2.place(rely=1, relx=0.0, x=0, y=0, anchor="sw")

# info button------------------------------------------------

photo3 = PhotoImage(file=r"info.png")
button3 = Button(var, image=photo3, compound=RIGHT,
                 borderwidth=0, command=var.destroy)
button3.place(rely=1, relx=0.1, x=0, y=0, anchor="sw")

# logo------------------------------------------------
image = Image.open("logo.png")

# Resizing the logo
resized_image = image.resize((65, 65), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
label1 = Label(var, image=new_image)
label1.image_names = new_image
label1.place(relx=0.8, y=15)

# grid ----------------------------------------------
galleryContainer = Canvas(var, width=460, height=450, bg="white")
galleryContainer.place(relx=0.5, rely=0.539, anchor="center")

# create grid

galleryGrid1 = Canvas(galleryContainer, bg="white", width=150, height=150)
galleryGrid1.place(relx=0, rely=0)

galleryGrid2 = Canvas(galleryContainer, bg="white", width=150, height=150)
galleryGrid2.place(relx=0.33, rely=0)

galleryGrid3 = Canvas(galleryContainer, bg="white", width=150, height=150)
galleryGrid3.place(relx=0.66, rely=0)

galleryGrid4 = Canvas(galleryContainer, bg="white", width=150, height=150)
galleryGrid4.place(relx=0, rely=0.33)

galleryGrid5 = Canvas(galleryContainer, bg="white", width=150, height=150)
galleryGrid5.place(relx=0.33, rely=0.33)

galleryGrid6 = Canvas(galleryContainer, bg="white", width=150, height=150)
galleryGrid6.place(relx=0.66, rely=0.33)

galleryGrid7 = Canvas(galleryContainer, bg="white", width=150, height=150)
galleryGrid7.place(relx=0, rely=0.66)

galleryGrid8 = Canvas(galleryContainer, bg="white", width=150, height=150)
galleryGrid8.place(relx=0.33, rely=0.66)

galleryGrid9 = Canvas(galleryContainer, bg="white", width=150, height=150)
galleryGrid9.place(relx=0.66, rely=0.66)

galleryGrid = [galleryGrid1, galleryGrid2, galleryGrid3, galleryGrid4,
               galleryGrid5, galleryGrid6, galleryGrid7, galleryGrid8, galleryGrid9]


images = list(map(lambda x: f"{active}/{x}", os.listdir(f"{active}/")))
rand_images = []

for folder in os.listdir():
    if len(folder.split("."))==1 and folder.split(".")[0] !=active:
        rand_images.extend([f"{folder}/{image}" for image in os.listdir(folder)])

random.shuffle(rand_images)
rand_images = rand_images[:5]
rand_images.extend(images)
random.shuffle(rand_images)

position = []
for i in range(len(rand_images)):
    if rand_images[i] in images:
        position.append(i)

# gallery for the images

image_lust = [ImageTk.PhotoImage(Image.open(rand_images[i]).resize((148,148))) for i in range(9)]

# for i in range(9):
    # Button(galleryGrid[i],text="",image=image_lust[i], command=lambda:fun(i)).place(relx=0.5, rely=0.5, anchor="center")
    
Button(master=galleryGrid[0],text=str(0),image=image_lust[0], command=lambda:fun(0)).place(relx=0.5, rely=0.5, anchor="center")
Button(master=galleryGrid[1],text=str(1),image=image_lust[1], command=lambda:fun(1)).place(relx=0.5, rely=0.5, anchor="center")
Button(master=galleryGrid[2],text=str(2),image=image_lust[2], command=lambda:fun(2)).place(relx=0.5, rely=0.5, anchor="center")
Button(master=galleryGrid[3],text=str(3),image=image_lust[3], command=lambda:fun(3)).place(relx=0.5, rely=0.5, anchor="center")
Button(master=galleryGrid[4],text=str(4),image=image_lust[4], command=lambda:fun(4)).place(relx=0.5, rely=0.5, anchor="center")
Button(master=galleryGrid[5],text=str(5),image=image_lust[5], command=lambda:fun(5)).place(relx=0.5, rely=0.5, anchor="center")
Button(master=galleryGrid[6],text=str(6),image=image_lust[6], command=lambda:fun(6)).place(relx=0.5, rely=0.5, anchor="center")
Button(master=galleryGrid[7],text=str(7),image=image_lust[7], command=lambda:fun(7)).place(relx=0.5, rely=0.5, anchor="center")
Button(master=galleryGrid[8],text=str(8),image=image_lust[8], command=lambda:fun(8)).place(relx=0.5, rely=0.5, anchor="center")
  
var.mainloop()
