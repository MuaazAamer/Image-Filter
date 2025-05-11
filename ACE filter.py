import tkinter as tk
import numpy as np
from PIL import Image, ImageTk

# Load the input image
input_image1 = Image.open('img2.jpg')
input_image=input_image1.resize((300,300))
input_image = input_image.convert('L')  # Convert to grayscale


# Create a Tkinter window
window = tk.Tk()

# Create labels and entry widgets for the user to input the window size, k1, and k2 values
window_size_label = tk.Label(window, text="Window size:")
window_size_label.pack()
window_size_entry = tk.Entry(window)
window_size_entry.pack()

k1_label = tk.Label(window, text="k1:")
k1_label.pack()
k1_entry = tk.Entry(window)
k1_entry.pack()

k2_label = tk.Label(window, text="k2:")
k2_label.pack()
k2_entry = tk.Entry(window)
k2_entry.pack()

# Create a PhotoImage object from the input image
input_image_tk = ImageTk.PhotoImage(input_image)

# Create a label to display the input image
input_image_label = tk.Label(window, image=input_image_tk)
#input_image_label.pack()

# Define the ACE filter function
def ace_filter(image, kernel_size, k1, k2):
    # Create an empty output image
    output_image = np.zeros(image.shape, dtype=np.uint8)

    # Iterate over each pixel in the image
    for r in range(kernel_size//2, image.shape[0] - kernel_size//2):
        for c in range(kernel_size//2, image.shape[1] - kernel_size//2):
           # Calculate the local mean and standard deviation in the current nxn window
            window = image[r-kernel_size//2:r+kernel_size//2+1, c-kernel_size//2:c+kernel_size//2+1]
            m1 = np.mean(window)
            sigma = np.std(window)

            # Calculate the ACE filter output for the current pixel
            output_image[r, c] = k1 * k2 * m1 + (1 - k1 * k2) * image[r, c] if sigma > 0 else image[r, c]

    return output_image

# Define a function to apply the ACE filter when the user clicks a button
def apply_ace_filter():
    # Get the user input for the window size, k1, and k2 values
    kernel_size = int(window_size_entry.get())
    k1 = float(k1_entry.get())
    k2 = float(k2_entry.get())

    # Apply the ACE filter to the input image
    output_image = ace_filter(np.array(input_image), kernel_size, k1, k2)

    # Convert the output image to a PIL Image object
    output_image = Image.fromarray(output_image)

    # Create a PhotoImage object from the output image
    output_image_tk = ImageTk.PhotoImage(output_image)

    # Update the output image label with the new image
    output_image_label.config(image=output_image_tk)
    output_image_label.image = output_image_tk

    # Save the output image to a file
    output_image.save('output_image.jpg')

# Create a button to apply the ACE filter
apply_button = tk.Button(window, text="Apply ACE Filter", command=apply_ace_filter)
apply_button.pack()

# Create a label to display the output image
output_image_label = tk.Label(window, image=input_image_tk)
output_image_label.pack()

# Start the Tkinter eventloop
window.mainloop()