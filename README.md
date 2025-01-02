# QR Code Generator

This repository contains two Python programs for generating QR codes:

1. **main.py**: A command-line application for generating QR codes.
2. **main_2.py**: A graphical user interface (GUI) application for generating QR codes with enhanced visuals.

## Features

### main.py (Terminal Version)
- Simple and lightweight.
- Accepts user input (text or URL) via the terminal.
- Generates a QR code and saves it as an image file.

### main_2.py (GUI Version)
- User-friendly interface built with `tkinter`.
- Provides input fields and buttons for interaction.
- Allows users to preview the generated QR code within the application.
- Supports custom file naming and saving options.

## Requirements

Both applications require the following Python libraries:

- `qrcode`
- `Pillow` (for image processing in the GUI version)

Install the required libraries using:
```bash
pip install qrcode[pil] pillow
```

## How to Use

### 1. Running the Terminal Version

1. Open a terminal or command prompt.
2. Run the `main.py` script:
   ```bash
   python main.py
   ```
3. Enter the text or URL to generate a QR code.
4. Specify the output file name (e.g., `qrcode.png`).
5. The QR code will be saved to the specified location.

### 2. Running the GUI Version

1. Run the `main_2.py` script:
   ```bash
   python main_2.py
   ```
2. Enter the text or URL in the provided input field.
3. Click the **Generate QR Code** button.
4. Choose a location and file name to save the QR code image.
5. Preview the generated QR code within the application.

## Screenshots
![Screenshot_1](https://github.com/user-attachments/assets/34fe994a-a34c-4b0e-b5ef-85e126bd50a5)

### GUI Version
![GUI Screenshot](https://via.placeholder.com/400x300.png?text=GUI+Preview)

## File Structure

```
|-- main.py        # Terminal-based QR code generator
|-- main_2.py      # GUI-based QR code generator
|-- README.md      # Documentation file
```

## Contributions

Contributions are welcome! Feel free to fork the repository and submit pull requests with improvements or new features.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

