import qrcode

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
        print(f"QR Code successfully saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the QR Code Generator!")
    text_or_url = input("Enter the text or URL to generate a QR code: ")
    output_filename = input("Enter the output filename (e.g., 'qrcode.png'): ")

    generate_qr_code(text_or_url, output_filename)
