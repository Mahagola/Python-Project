from tkinter import*
from tkinter import messagebox as msg
from PIL import Image, ImageTk
import random
import os

var = Tk()
var.title('ReCaptcha)
def main():
    
    global position,selected,rand_images
    var.geometry("480x610")
    var.minsize(height=610, width=480)
    var.maxsize(height=610, width=480)
    
    # grid --------------------------------------------------
    galleryContainer = Canvas(var, width=460, height=450, bg="white")
    galleryContainer.place(relx=0.5, rely=0.539, anchor="center")

    # create grid-------------------------------------------- 

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

    galleryGrid = [galleryGrid1, galleryGrid2, galleryGrid3, galleryGrid4,galleryGrid5, galleryGrid6, galleryGrid7, galleryGrid8, galleryGrid9]
    
    # verify image button----------------------------------------
    button = Button(var, image=photo, compound=RIGHT,borderwidth=0, command=verify_captcha)
    button.place(rely=1, relx=0.98, x=0, y=0, anchor=SE)

    # reload button----------------------------------------------
    button2 = Button(var, image=photo2, compound=RIGHT,borderwidth=0, command=lambda:forget())
    button2.place(rely=1, relx=0.0, x=0, y=0, anchor="sw")

    # info button-----------------------------------------
    button3 = Button(var, image=photo3, compound=RIGHT,borderwidth=0, command=lambda:info_msg())
    button3.place(rely=1, relx=0.1, x=0, y=0, anchor="sw")

    # logo------------------------------------------------
    image = Image.open("./icons/logo.png")

    # Resizing the logo-----------------------------------
    resized_image = image.resize((65, 65), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    label1 = Label(var, image=new_image)
    label1.image_names = new_image
    label1.place(relx=0.8, y=15)
    
    # to call active images-------------------------------------------
    active = random.choice(["cats", "hydrant", "stairs", "traffic-lights"])
    
    # heading part---------------------------------------------------
    Label(var, text="Select all images with ", font=('verdana', 23)).pack(
        side=TOP, pady=4, padx=15, anchor='w')
    
    # change text according to images --------------------------------
    Label(var, text=f"{active}".upper(), font=('verdana', 24, 'bold')).pack(side=TOP, pady=3, padx=20, anchor='nw')
    active_images = list(map(lambda x: f"./images/{active}/{x}", os.listdir(f"./images/{active}/")))
    
    
    # to store random images------------------------------------------     
    rand_images = []

    for folder in os.listdir('./images'):
        if len(folder.split("."))==1 and folder.split(".")[0]!=active:
            rand_images.extend([f"./images/{folder}/{image}" for image in os.listdir(f'./images/{folder}')])
    random.shuffle(rand_images)
    rand_images = rand_images[:5]
    rand_images.extend(active_images) 
    random.shuffle(rand_images)
    
    
    position = [] # to store the position of active images
    for i in range(len(rand_images)):
        if rand_images[i] in active_images:
            position.append(i)


    # gallery for the images---------------------------------------------------------------
    createImage_list()    
    Button(master=galleryGrid[0],text=str(0),image=image_list[0],bd=0, highlightthickness=0, command=lambda:validate(0, galleryGrid[0]), relief=FLAT).place(relx=0.5, rely=0.5, anchor="center")
    Button(master=galleryGrid[1],text=str(1),image=image_list[1],bd=0, highlightthickness=0, command=lambda:validate(1, galleryGrid[1]), relief=FLAT).place(relx=0.5, rely=0.5, anchor="center")
    Button(master=galleryGrid[2],text=str(2),image=image_list[2],bd=0, highlightthickness=0, command=lambda:validate(2, galleryGrid[2]), relief=FLAT).place(relx=0.5, rely=0.5, anchor="center")
    Button(master=galleryGrid[3],text=str(3),image=image_list[3],bd=0, highlightthickness=0, command=lambda:validate(3, galleryGrid[3]), relief=FLAT).place(relx=0.5, rely=0.5, anchor="center")
    Button(master=galleryGrid[4],text=str(4),image=image_list[4],bd=0, highlightthickness=0, command=lambda:validate(4, galleryGrid[4]), relief=FLAT).place(relx=0.5, rely=0.5, anchor="center")
    Button(master=galleryGrid[5],text=str(5),image=image_list[5],bd=0, highlightthickness=0, command=lambda:validate(5, galleryGrid[5]), relief=FLAT).place(relx=0.5, rely=0.5, anchor="center")
    Button(master=galleryGrid[6],text=str(6),image=image_list[6],bd=0, highlightthickness=0, command=lambda:validate(6, galleryGrid[6]), relief=FLAT).place(relx=0.5, rely=0.5, anchor="center")
    Button(master=galleryGrid[7],text=str(7),image=image_list[7],bd=0, highlightthickness=0, command=lambda:validate(7, galleryGrid[7]), relief=FLAT).place(relx=0.5, rely=0.5, anchor="center")
    Button(master=galleryGrid[8],text=str(8),image=image_list[8],bd=0, highlightthickness=0, command=lambda:validate(8, galleryGrid[8]), relief=FLAT).place(relx=0.5, rely=0.5, anchor="center")  

# to store selected images----------------------------------
selected=[]

photo = PhotoImage(file=r"./icons/check.png")
photo2 = PhotoImage(file=r"./icons/reload.png")
photo3 = PhotoImage(file=r"./icons/info.png")

image_list=[]
rand_images=[]

def forget():
    global selected,position
    for widget in var.winfo_children():   
       widget.place_forget()
       widget.pack_forget()
       widget.grid_forget()
    selected=[]
    position = []
    main() #recalling the function again--------------------------------------

def validate(pos, parent):
    global selected
    if pos in selected:
        selected.remove(pos)
        parent["bg"] = "white"
    else:
        selected.append(pos)
        parent["bg"] = "#1fceff"
  
def verify_captcha():
    if sorted(position) == sorted(selected):
        msg.showinfo("Success", message="You completed verification successfully")
    else:
        msg.showerror("Unsuccessful", message="Try Again!!")
    forget()

def createImage_list():
    global image_list
    image_list = [ImageTk.PhotoImage(Image.open(rand_images[i]).resize((130,130))) for i in range(9)]
    
def info_msg():
    msg.showinfo("Hi", message="Please Select Valid Images!!")
    forget()

main()
var.mainloop()
