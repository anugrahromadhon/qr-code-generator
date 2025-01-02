import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

def generate_qr_code(data, output_file):
    """
    Generate a QR code for the given data and save it as an image file.

    Parameters:
        data (str): The text or URL to encode in the QR code.
        output_file (str): The name of the output file (e.g., 'qrcode.png').
    """
    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code, 1 is 21x21
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in pixels
            border=4,  # Minimum border size in boxes
        )

        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image of the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image
        img.save(output_file)
        return output_file
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    return file_path

def generate_qr():
    data = entry_data.get()
    if not data:
        messagebox.showwarning("Input Required", "Please enter text or URL to generate QR code.")
        return

    output_file = save_file()
    if output_file:
        result = generate_qr_code(data, output_file)
        if result:
            messagebox.showinfo("Success", f"QR Code saved to {result}")
            display_qr(result)

def display_qr(file_path):
    try:
        img = Image.open(file_path)
        img = img.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        qr_label.configure(image=img)
        qr_label.image = img
    except Exception as e:
        messagebox.showerror("Error", f"Unable to display QR code: {e}")

# Create the GUI application
app = tk.Tk()
app.title("QR Code Generator")
app.geometry("400x400")
app.configure(bg="#f0f8ff")

# Title label
title_label = tk.Label(app, text="QR Code Generator", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#2f4f4f")
title_label.pack(pady=10)

# Input field and label
input_frame = tk.Frame(app, bg="#f0f8ff")
input_frame.pack(pady=10)

entry_label = tk.Label(input_frame, text="Enter text or URL:", font=("Arial", 12), bg="#f0f8ff", fg="#2f4f4f")
entry_label.pack(side=tk.LEFT, padx=5)

entry_data = tk.Entry(input_frame, width=30, font=("Arial", 12))
entry_data.pack(side=tk.LEFT, padx=5)

# Generate button
generate_button = tk.Button(app, text="Generate QR Code", font=("Arial", 12, "bold"), bg="#4682b4", fg="white", command=generate_qr)
generate_button.pack(pady=20)

# QR Code display
qr_label = tk.Label(app, bg="#f0f8ff")
qr_label.pack(pady=10)

# Run the GUI event loop
app.mainloop()
