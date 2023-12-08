# import modules
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font 
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image,ImageTk,ImageFilter,ImageEnhance,ImageOps
import PIL
import os

editor = Tk()
editor.title("Photo Editor - By Mahaveer")
editor.minsize(width=800,height=520)
editor.maxsize(width=800,height=520)
editor.config(bg="white")
icon = PhotoImage(file='icon.png')

editor.iconphoto(False,icon)

rotate_value = DoubleVar()
blur_value = IntVar()
bright_value=IntVar()
border_value=IntVar()
contrast_value =IntVar()


'''''''''''''''''''''''''''''''''''
    Funcitons
'''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''
Open Function - For Open file
'''''''''''''''''''''''''''''''''''
def open():
    global image_path, original_image, tk_img 

    image_path = filedialog.askopenfilename(initialdir=os.getcwd())
    original_image = Image.open(image_path)
    original_image.thumbnail((450,450))
    tk_img = ImageTk.PhotoImage(original_image)
    before_canvas.create_image(150, 150, image=tk_img)
    before_canvas.image=original_image

'''''''''''''''''''''''''''''''''''
Save Function - For save file
'''''''''''''''''''''''''''''''''''
rotated_tk_img=None
blur_tk_img=None
bright_tk_img=None
border_tk_img=None
flip_tk_img=None
flip_tb_tk_img=None
def save():
    ext = image_path.split(".")[-1]
    file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
    if file:
        if after_canvas.image==rotated_tk_img:
            rotated_img.save(file)
        elif after_canvas.image==blur_tk_img:
            blur_img.save(file)
        elif after_canvas.image==bright_tk_img:
            brighten_img.save(file)
        elif after_canvas.image==border_tk_img:
            border_img.save(file)
        elif after_canvas.image==flip_tk_img:
            flip_img.save(file)
        elif after_canvas.image==flip_tb_tk_img:
            flip_tb_img.save(file)
        elif after_canvas.image==contrast_tk_img:
            contrasted_img.save(file)
'''''''''''''''''''''''''''''''''''
Rotate Function - For rotate image
'''''''''''''''''''''''''''''''''''

def rotate():
    
    global image_path ,rotated_img,rotated_tk_img
    original_image = Image.open(image_path)
    original_image.thumbnail((450,450))
    rotated_img = original_image.rotate(int(rotate_value.get()))
    rotated_tk_img = ImageTk.PhotoImage(rotated_img)
    after_canvas.create_image(150, 150, image=rotated_tk_img)
    after_canvas.image=rotated_tk_img
    rotate_frame = Toplevel()
    rotate_frame.title("Rotate - Photo Editor")
    
    '''''''''''''''''
    input scales
    '''''''''''''''''
    def get_current_value():
        return '{: .2f}'.format(int(rotate_value.get()))

    def scale_value(event):
        label2.config(text=get_current_value())
    scale3 = ttk.Scale(rotate_frame,length=300, from_=0, to=360, variable=rotate_value, orient=HORIZONTAL, command=scale_value) 
    scale3.pack()
    label2=Label(rotate_frame,text="value")
    label2.pack(side=TOP)
    '''''''''''''''''''''''''''
    input scales
    '''''''''''''''''''''''''''
    
    rotate_frame.mainloop()
    rotate_frame.quit()
'''''''''''''''''''''''''''''''''''
Blur Function - For blur image
'''''''''''''''''''''''''''''''''''
def blur():
    global image_path, blur_tk_img, blur_img
    for m in range(0, blur_value.get()+1):
            original_image = Image.open(image_path)
            original_image.thumbnail((450,450))
            blur_img = original_image.filter(ImageFilter.BoxBlur(m))
            blur_tk_img = ImageTk.PhotoImage(blur_img)
    after_canvas.create_image(150, 150, image=blur_tk_img)
    after_canvas.image=blur_tk_img

    blur_frame = Toplevel()
    blur_frame.title("Blur - Photo Editor")
    
    '''''''''''''''''
    input scales -Start
    '''''''''''''''''
    def get_current_value():
        return '{: .2f}'.format(int(blur_value.get()))

    def scale_value(event):
        label2.config(text=get_current_value())
    scale3 = ttk.Scale(blur_frame,length=300, from_=0, to=360, variable=blur_value, orient=HORIZONTAL, command=scale_value) 
    scale3.pack()
    label2=Label(blur_frame,text="value")
    label2.pack(side=TOP)
    '''''''''''''''''''''''''''
    input scales
    '''''''''''''''''''''''''''
    
    blur_frame.mainloop()
    blur_frame.quit()
'''''''''''''''''''''''''''''''''''
Brightness  Function - For brighten image
'''''''''''''''''''''''''''''''''''
def brightness():
    global image_path, bright_img,brighten_img ,bright_tk_img
    for m in range(0, bright_value.get()+1):
            original_image = Image.open(image_path)
            original_image.thumbnail((450,450))
            bright_img = ImageEnhance.Brightness(original_image)
            brighten_img=bright_img.enhance(m)
            bright_tk_img = ImageTk.PhotoImage(brighten_img)
            after_canvas.create_image(150, 150, image=bright_tk_img)
            after_canvas.image=bright_tk_img
    
    bright_frame = Toplevel()
    bright_frame.title("Brightness - Photo Editor")
    
    '''''''''''''''''
    input scales -Start
    '''''''''''''''''
    def get_current_value():
        return '{: .2f}'.format(int(bright_value.get()))

    def scale_value(event):
        label2.config(text=get_current_value())
    scale3 = ttk.Scale(bright_frame,length=300, from_=0, to=360, variable=bright_value, orient=HORIZONTAL, command=scale_value) 
    scale3.pack()
    label2=Label(bright_frame,text="value")
    label2.pack(side=TOP)
    '''''''''''''''''''''''''''
    input scales
    '''''''''''''''''''''''''''
    
    bright_frame.mainloop()
    bright_frame.quit()
'''''''''''''''''''''''''''''''''''
Border Function - For add border on image
'''''''''''''''''''''''''''''''''''
def border():
    global image_path, border_img, border_tk_img
    original_image = Image.open(image_path)
    original_image.thumbnail((350, 350))
    
    border_img = ImageOps.expand(original_image,border=border_value.get(),fill=95)
    border_tk_img = ImageTk.PhotoImage(border_img)

    after_canvas.create_image(150, 150, image=border_tk_img)
    after_canvas.image=border_tk_img
    
    border_frame = Toplevel()
    border_frame.title("Border - Photo Editor")
    
    '''''''''''''''''
    input scales -Start
    '''''''''''''''''
    def get_current_value():
        return '{: .2f}'.format(int(border_value.get()))

    def scale_value(event):
        label2.config(text=get_current_value())
    scale3 = ttk.Scale(border_frame,length=300, from_=0, to=360, variable=border_value, orient=HORIZONTAL, command=scale_value) 
    scale3.pack()
    label2=Label(border_frame,text="value")
    label2.pack(side=TOP)
    '''''''''''''''''''''''''''
    input scales
    '''''''''''''''''''''''''''
    
    border_frame.mainloop()
    border_frame.quit()
'''''''''''''''''''''''''''''''''''
flip_left_right Function - For flip the image from left to right
'''''''''''''''''''''''''''''''''''
def flip_left_right():
    global image_path, flip_img, flip_tk_img
    original_image = Image.open(image_path)
    original_image.thumbnail((350, 350))
    flip_img = original_image.transpose(Image.FLIP_LEFT_RIGHT)
    flip_tk_img = ImageTk.PhotoImage(flip_img)
    after_canvas.create_image(300, 210, image=flip_tk_img)
    after_canvas.image=flip_tk_img
'''''''''''''''''''''''''''''''''''
flip_top_bottom Function - For flip the image from top to bottom
'''''''''''''''''''''''''''''''''''
def flip_top_bottom():
    global image_path, flip_tb_img, flip_tb_tk_img
    original_image = Image.open(image_path)
    original_image.thumbnail((350, 350))
    flip_tb_img = original_image.transpose(Image.FLIP_TOP_BOTTOM)
    flip_tb_tk_img = ImageTk.PhotoImage(flip_tb_img)
    after_canvas.create_image(300, 210, image=flip_tb_tk_img)
    after_canvas.image=flip_tb_tk_img
'''''''''''''''''''''''''''''''''''
Contrast Function - For increase the contrast on the image
'''''''''''''''''''''''''''''''''''
def contrast():
    global contrasted_img,contrast_tk_img
    original_image = Image.open(image_path)
    original_image.thumbnail((350, 350))
    for m in range(0, contrast_value.get()+1):
            contrast_img = ImageEnhance.Contrast(original_image)
            contrasted_img = contrast_img.enhance(m)
            contrast_tk_img = ImageTk.PhotoImage(contrasted_img)
            after_canvas.create_image(300, 210, image=contrast_tk_img)
            after_canvas.image=contrast_tk_img
    contrast_frame = Toplevel()
    contrast_frame.title("Contrast - Photo Editor")
    
    '''''''''''''''''
    input scales -Start
    '''''''''''''''''
    def get_current_value():
        return '{: .2f}'.format(int(contrast_value.get()))

    def scale_value(event):
        label2.config(text=get_current_value())
    scale3 = ttk.Scale(contrast_frame,length=300, from_=0, to=360, variable=contrast_value, orient=HORIZONTAL, command=scale_value) 
    scale3.pack()
    label2=Label(contrast_frame,text="value")
    label2.pack(side=TOP)
    '''''''''''''''''''''''''''
    input scales
    '''''''''''''''''''''''''''
    
    contrast_frame.mainloop()
    contrast_frame.quit()

'''''''''''''''''''''''''''''''''''
    Menu 
'''''''''''''''''''''''''''''''''''
# Menu
menubar = Menu(editor)
# File Menu
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Open",command=open)
filemenu.add_command(label="Save",command=save)
filemenu.add_command(label="Exit",command=editor.quit)
# add file menu in Main Menu
menubar.add_cascade(label="File",menu=filemenu)

editor.config(menu=menubar)

'''''''''''''''''''''''''''''''''''
    Frame for canvas
'''''''''''''''''''''''''''''''''''
canvas_frame=Frame(editor)
canvas_frame.grid(row=0,column=0,columnspan=5)

'''''''''''''''''''''''''''''''''''
    First Canvas Frame 
'''''''''''''''''''''''''''''''''''

before_canvas = Canvas(canvas_frame,height=400,width=400,bg="white")
b_canvas_title = before_canvas.create_text(100,20,text="Original",fill="#14274E",font=('arial 14 bold'))

img_canvas = before_canvas.create_image(10,10,anchor=NW)
before_canvas.pack(side=LEFT)

'''''''''''''''''''''''''''''''''''
    Second canvas Frame
'''''''''''''''''''''''''''''''''''

after_canvas = Canvas(canvas_frame,height=400,width=400,bg="white")
a_canvas_title = after_canvas.create_text(100,20,text="Edited",fill="#14274E",font=('arial 14 bold'))

img_canvas = after_canvas.create_image(30,30,anchor=NW)
after_canvas.pack(side=LEFT)
'''''''''''''''''
    Rotate frame
'''''''''''''''''

'''''''''''''''''''''''''''''''''''
    Frame for Button
'''''''''''''''''''''''''''''''''''
button_frame=Frame(editor,bg="white")
button_frame.grid(row=1,column=0,columnspan=5,pady=5)

'''''''''''''''''
    Features Buttons
'''''''''''''''''

rotate_button = Button(button_frame,text="Rotate",fg="#14274E",font=('arial 12 bold'),bg="#F1F6F9",border=0,command=rotate)
rotate_button.grid(row=0,column=0,ipadx=5,padx=5)
blur_button = Button(button_frame,text="Blur",fg="#14274E",font=('arial 12 bold'),bg="#F1F6F9",border=0,command=blur)
blur_button.grid(row=0,column=1,ipadx=5,padx=5)
brightness_button = Button(button_frame,text="Brightness",fg="#14274E",font=('arial 12 bold'),bg="#F1F6F9",border=0,command=brightness)
brightness_button.grid(row=0,column=2,ipadx=5,padx=5)
border_button = Button(button_frame,text="Border",fg="#14274E",font=('arial 12 bold'),bg="#F1F6F9",border=0,command=border)
border_button.grid(row=0,column=3,ipadx=5,padx=5)
LR_button = Button(button_frame,text="Flip L-R",fg="#14274E",font=('arial 12 bold'),bg="#F1F6F9",border=0,command=flip_left_right)
LR_button.grid(row=0,column=4,ipadx=5,padx=5)
TB_button = Button(button_frame,text="Flip T-B",fg="#14274E",font=('arial 12 bold'),bg="#F1F6F9",border=0,command=flip_top_bottom)
TB_button.grid(row=0,column=5,ipadx=5,padx=5)
contrast_button = Button(button_frame,text="Contrast",fg="#14274E",font=('arial 12 bold'),bg="#F1F6F9",border=0,command=contrast)
contrast_button.grid(row=0,column=6,ipadx=5,padx=5)


'''''''''''''''''''''''''''''''''''
    Frame for Creadit
'''''''''''''''''''''''''''''''''''

credit_frame=Frame(editor,bg="white")
credit_frame.grid(row=2,column=0,columnspan=5,pady=10)

'''''''''''''''''''''''''''''''''''
    Creadit
'''''''''''''''''''''''''''''''''''
open_button = Button(credit_frame,text="Open",fg="#ffffff",font=('arial 13 bold'),bg="#14274E",border=0,command=open)
open_button.grid(row=0,column=0,ipadx=10,padx=5)
save_button = Button(credit_frame,text="save",fg="#ffffff",font=('arial 13 bold'),bg="#14274E",border=0,command=save)
save_button.grid(row=0,column=1,ipadx=10,padx=5)
quit_button = Button(credit_frame,text="Exit",fg="#ffffff",font=('arial 13 bold'),bg="#14274E",border=0,command=editor.quit)
quit_button.grid(row=0,column=2,ipadx=10,padx=5)

credit = Label(credit_frame,text="Design and Developed By Mahaveer",bg="white",fg="#14274E")
credit.grid(row=1,column=0,columnspan=5)
'''''''''''''''''''''''''''''''''''
    Calling mainloop() function with editor object
'''''''''''''''''''''''''''''''''''

editor.mainloop()

