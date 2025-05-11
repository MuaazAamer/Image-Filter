import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from tkinter import *
import numpy as np
import cv2
from PIL import Image, ImageTk
import math

image = None
greyscale_image = None
color_image=None
# ------------------------------ Pseudo Coloring -----------------------------



def Pseudo_Color(image, r11=0, r12=64, r21=64, r22=128, r31=128, r32=192, r41=192, r42=255, r1=0, g1=0, b1=255, r2=0, g2=255, b2=0, r3=255, g3=0, b3=0, r4=0, g4=0, b4=0):
    np_image = np.array(image)
    rows, cols = np_image.shape

    color_image = np.zeros((rows, cols, 3), dtype=np.uint8)

    ranges = [
        ((r11, r12), (r1, g1, b1)),     # Range 1
        ((r21, r22), (r2, g2, b2)),   # Range 2
        ((r31, r32), (r3, g3, b3)),  # Range 3
        ((r41, r42), (r4, g4, b4))  # Range 4
    ]

    for i in range(rows):
        for j in range(cols):
            for (start, end), (r_val, g_val, b_val) in ranges:
                if start <= np_image[i, j] < end:
                    color_image[i, j] = [r_val, g_val, b_val]
                    break

    pseudoimage = ImageTk.PhotoImage(image=Image.fromarray(color_image))
    pseudoimage_label = ttk.Label(image_frame)
    pseudoimage_label.config(image=pseudoimage)
    pseudoimage_label.image = pseudoimage
    pseudoimage_label.grid(column=3, row=0, sticky='w')
  

def Pseudo_Color_Button():
    global greyscale_image, Slice1_from, Slice1_to, Slice2_from, Slice2_to, Slice3_from, Slice3_to, Slice4_from, Slice4_to, r1, g1, b1, r2, g2, b2, r3, g3, b3, r4, g4, b4
    if greyscale_image:
        Pseudo_Color(greyscale_image, Slice1_from.get(), Slice1_to.get(), Slice2_from.get(), Slice2_to.get(),
                     Slice3_from.get(), Slice3_to.get(), Slice4_from.get(), Slice4_to.get(),
                     r1.get(), g1.get(), b1.get(), r2.get(), g2.get(), b2.get(),
                     r3.get(), g3.get(), b3.get(), r4.get(), g4.get(), b4.get())
    else:
        print("Please select an image first")



def upload_picture():
    global image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        try:
            image = Image.open(file_path)
            image = image.resize((300, 300))
            image_tk = ImageTk.PhotoImage(image)
            image_label.config(image=image_tk)
            image_label.image = image_tk
        except Exception as e:
            print(f"Error uploading image: {e}")

def grey_scale():
    global greyscale_image
    if image:
        greyscale_image = image.convert('L')
        greyscale_image = greyscale_image.resize((300, 300))
        greyscale_image_tk = ImageTk.PhotoImage(greyscale_image)


        # Create a label for the grayscale image
        greyscale_label = ttk.Label(image_frame)
        greyscale_label.config(image=greyscale_image_tk)
        greyscale_label.image = greyscale_image_tk
        greyscale_label.grid(column=0,row=0,sticky="w")
        
root = tk.Tk()
root.title("ass2_gui")

# Create a frame for the operations
operations_frame = ttk.LabelFrame(root, text="Operations")
operations_frame.grid(column=0, row=0, padx=10, pady=10, sticky="w")

upload_picture_button = ttk.Button(operations_frame, text="Upload Picture")
upload_picture_button.grid(column=0, row=0, padx=10, pady=10)
upload_picture_button.config(command=upload_picture)

grey_scale_button = ttk.Button(operations_frame, text="Grey Scale", command=grey_scale)
grey_scale_button.grid(column=1, row=0, padx=10, pady=10)




# Create a frame for the intensity slicing options
intensity_slicing_frame = ttk.LabelFrame(root, text="Intensity Slicing")
intensity_slicing_frame.grid(column=0, row=1, padx=10, pady=10, sticky="w")

Slice1_from = tk.IntVar()
Slice1_from.set(0)
Slice1_to = tk.IntVar()
Slice1_to.set(0)
ttk.Label(intensity_slicing_frame, text="Slice1").grid(column=0, row=1, padx=10, pady=10, sticky="w")
ttk.Entry(intensity_slicing_frame, textvariable=Slice1_from).grid(column=1, row=1, padx=10, pady=10, sticky="w")
ttk.Label(intensity_slicing_frame, text="To").grid(column=2, row=1)
ttk.Entry(intensity_slicing_frame, textvariable=Slice1_to).grid(column=3, row=1)

Slice2_from = tk.IntVar()
Slice2_from.set(0)
Slice2_to = tk.IntVar()
Slice2_to.set(0)
ttk.Label(intensity_slicing_frame, text="Slice2").grid(column=0, row=2, padx=10, pady=10, sticky="w")
ttk.Entry(intensity_slicing_frame, textvariable=Slice2_from).grid(column=1, row=2, padx=10, pady=10, sticky="w")
ttk.Label(intensity_slicing_frame, text="To").grid(column=2, row=2)
ttk.Entry(intensity_slicing_frame, textvariable=Slice2_to).grid(column=3, row=2)

Slice3_from = tk.IntVar()
Slice3_from.set(0)
Slice3_to = tk.IntVar()
Slice3_to.set(0)
ttk.Label(intensity_slicing_frame, text="Slice3").grid(column=0, row=3, padx=10, pady=10, sticky="w")
ttk.Entry(intensity_slicing_frame, textvariable=Slice3_from).grid(column=1, row=3, padx=10, pady=10, sticky="w")
ttk.Label(intensity_slicing_frame, text="To").grid(column=2, row=3)
ttk.Entry(intensity_slicing_frame, textvariable=Slice3_to).grid(column=3, row=3)


Slice4_from = tk.IntVar()
Slice4_from.set(0)
Slice4_to = tk.IntVar()
Slice4_to.set(0)
ttk.Label(intensity_slicing_frame, text="Slice4").grid(column=0, row=4, padx=10, pady=10, sticky="w")
ttk.Entry(intensity_slicing_frame, textvariable=Slice4_from).grid(column=1, row=4, padx=10, pady=10, sticky="w")
ttk.Label(intensity_slicing_frame, text="To").grid(column=2, row=4, padx=10)
ttk.Entry(intensity_slicing_frame, textvariable=Slice4_to).grid(column=3, row=4)

red_frame=ttk.LabelFrame(root,text="Red")
red_frame.grid(column=2,row=1,padx=10, pady=10,sticky="w")

blue_frame=ttk.LabelFrame(root,text="Blue")
blue_frame.grid(column=3,row=1,padx=10, pady=10,sticky="w")

green_frame=ttk.LabelFrame(root,text="Green")
green_frame.grid(column=4,row=1,padx=10, pady=10,sticky="w")

#----------Red Values---------------------
r1=tk.IntVar()
r1.set(0)
ttk.Entry(red_frame, textvariable=r1).grid(column=2, row=1, padx=10, pady=10, sticky="w")
r2=tk.IntVar()
r2.set(0)
ttk.Entry(red_frame, textvariable=r2).grid(column=2, row=2, padx=10, pady=10, sticky="w")
r3=tk.IntVar()
r3.set(0)
ttk.Entry(red_frame, textvariable=r3).grid(column=2, row=3, padx=10, pady=10, sticky="w")
r4=tk.IntVar()
r4.set(0)
ttk.Entry(red_frame, textvariable=r4).grid(column=2, row=4, padx=10, pady=10, sticky="w")

#-------------Blue Values-------------------
b1=tk.IntVar()
b1.set(0)
ttk.Entry(blue_frame, textvariable=b1).grid(column=3, row=1, padx=10, pady=10, sticky="w")
b2=tk.IntVar()
b2.set(0)
ttk.Entry(blue_frame, textvariable=b2).grid(column=3, row=2, padx=10, pady=10, sticky="w")
b3=tk.IntVar()
b3.set(0)
ttk.Entry(blue_frame, textvariable=b3).grid(column=3, row=3, padx=10, pady=10, sticky="w")
b4=tk.IntVar()
b4.set(0)
ttk.Entry(blue_frame, textvariable=b4).grid(column=3, row=4, padx=10, pady=10, sticky="w")

#------------Green Values--------------------
g1=tk.IntVar()
g1.set(0)
ttk.Entry(green_frame, textvariable=g1).grid(column=4, row=1, padx=10, pady=10, sticky="w")
g2=tk.IntVar()
g2.set(0)
ttk.Entry(green_frame, textvariable=g2).grid(column=4, row=2, padx=10, pady=10, sticky="w")
g3=tk.IntVar()
g3.set(0)
ttk.Entry(green_frame, textvariable=g3).grid(column=4, row=3, padx=10, pady=10, sticky="w")
g4=tk.IntVar()
g4.set(0)
ttk.Entry(green_frame, textvariable=g4).grid(column=4, row=4, padx=10, pady=10, sticky="w")

#--------------------------------------------

Pseudocolor_button = ttk.Button(operations_frame, text="Pseudocolor",command=Pseudo_Color_Button)
Pseudocolor_button.grid(column=3, row=0, padx=10, pady=10)

image_frame=ttk.LabelFrame(root, text="Images")
image_frame.grid(column=0, row=4, padx=5, pady=5, sticky="w")

image_label = ttk.Label(image_frame)
image_label.grid(column=0, row=0, sticky="w")


root.mainloop()