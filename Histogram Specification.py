import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

def histogram_specification():
    global img1, img2, result_label
    if img1 is None or img2 is None:
        messagebox.showerror("Error", "Please load two images first.")
        return

    # Convert images to NumPy arrays
    img1_arr = np.array(img1)
    img2_arr = np.array(img2)

    # Calculate histograms
    hist1, _ = np.histogram(img1_arr.flatten(), bins=256, range=[0,256])
    hist2, _ = np.histogram(img2_arr.flatten(), bins=256, range=[0,256])

    # Calculate cumulative distribution functions (CDFs)
    cdf1 = hist1.cumsum()
    cdf2 = hist2.cumsum()

    # Normalize CDFs
    cdf1 = (cdf1 - cdf1.min()) * 255 / (cdf1.max() - cdf1.min())
    cdf2 = (cdf2 - cdf2.min()) * 255 / (cdf2.max() - cdf2.min())

    # Interpolation
    img1_eq = np.interp(img1_arr.flatten(), np.arange(0,256), cdf1).reshape(img1_arr.shape)
    img2_spec = np.interp(img1_eq.flatten(), cdf2, np.arange(0, 256)).reshape(img1_arr.shape)
    result_img= Image.fromarray(img2_spec.astype(np.uint8))

    # Convert the resulting image to a PhotoImage instance
    result_img_tk = ImageTk.PhotoImage(result_img)

    # Display the result
    result_label.config(image=result_img_tk)
    result_label.image = result_img_tk

    result_img.save("result_image.jpg")

# GUI setup
root = tk.Tk()
root.title("Histogram Specification")

# Load images
img11 = Image.open("img1.jpg")
img1=img11.resize((200,200))
image1=ImageTk.PhotoImage(img1)
img22 = Image.open("img2.jpg")
img2=img22.resize((200,200))
image2=ImageTk.PhotoImage(img2)

img1_label = tk.Label(root, image=image1)
img1_label.grid(row=0,column=0)

img2_label = tk.Label(root, image=image2)
img2_label.grid(row=1,column=0)

spec_button = tk.Button(root, text="Histogram Specification", command=histogram_specification)
spec_button.grid(row=2,column=0)

result_label = tk.Label(root)
result_label.grid(row=4,column=0)

root.mainloop()