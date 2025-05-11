import tkinter as tk
import numpy as np
from PIL import Image, ImageTk

# Load the input image
input_image1 = Image.open('img2.jpg')
input_image = input_image1.resize((300, 300))
input_image = input_image.convert('L')  # Convert to grayscale

# Create a Tkinter window
window = tk.Tk()

k1_label = tk.Label(window, text="window size:")
k1_label.pack()
k1_entry = tk.Entry(window)
k1_entry.pack()

# Create a PhotoImage object from the input image
input_image_tk = ImageTk.PhotoImage(input_image)

# Create a label to display the input image
input_image_label = tk.Label(window, image=input_image_tk)
# input_image_label.pack()

def MMSE(image, window_size, noise_var):
    output_image = np.zeros_like(image)

    # Calculate the standard deviation of the noise
    noise_std = np.sqrt(noise_var)

    # Calculate the size of the window
    half_window_size = window_size // 2

    # Initialize the output image
    output_image = np.zeros_like(image)

    # Iterate over each pixel in the image
    for i in range(half_window_size, image.shape[0] - half_window_size):
        for j in range(half_window_size, image.shape[1] - half_window_size):
            # Get the window around the current pixel
            window = image[i - half_window_size:i + half_window_size + 1, j - half_window_size:j + half_window_size + 1]

            # Calculate the local mean and variance
            local_mean = np.mean(window)
            local_variance = np.var(window)

            # Calculate the MMSE estimate
            mmse = local_mean + (image[i, j] - local_mean) * (window_size ** 2) / (window_size ** 2 + local_variance + noise_var)

            # Set the output pixel value
            output_image[i, j] = mmse


    return output_image

def mmsefilter():
    # Get the user input for the window size, k1, and k2 values
    k1 = int(k1_entry.get())  # Convert to integer

    # Convert the input image to a NumPy array
    input_image_array = np.array(input_image)

    # Apply the MMSE filter to the noisy image
    output_image = MMSE(np.array(input_image_array), k1, 0.1)

    # Convert the output image to a PIL Image object
    output_image = Image.fromarray(output_image)

    # Create a PhotoImage object from the output image
    output_image_tk = ImageTk.PhotoImage(output_image)

    # Update the output image label with the new image
    output_image_label.config(image=output_image_tk)
    output_image_label.image = output_image_tk

    # Save the output image to a file
    output_image.save('MMSE.jpg')


# Create a button to apply the MMSE filter
apply_button = tk.Button(window, text="Apply MMSE filter",command=mmsefilter)
apply_button.pack()

# Create a label to display the output image
output_image_label = tk.Label(window, image=input_image_tk)
output_image_label.pack()

# Start the Tkinter eventloop
window.mainloop()