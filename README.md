# Photo Editor - By Mahaveer
A simple and user-friendly photo editor application built using Python and Tkinter. This photo editor allows users to perform various image processing tasks such as rotating, blurring, adjusting brightness, adding borders, flipping, and increasing contrast. It offers an intuitive graphical user interface (GUI) to make photo editing easy and accessible for all users.

![](https://maha-veer.github.io/assets/img/PhotoEditingApp.png)
## Features
- Open and Save Images: Open an image file from your system and save the edited image to a new location.
- Image Editing Functions:
    - Rotate: Rotate the image by any angle (0-360 degrees).
    - Blur: Apply blur effect to the image with adjustable blur intensity.
    - Brightness: Adjust the brightness of the image to make it lighter or darker.
    - Border: Add a customizable border around the image.
    - Flip Left-Right: Flip the image horizontally.
    - Flip Top-Bottom: Flip the image vertically.
    - Contrast: Increase or decrease the contrast of the image.
- Intuitive GUI: Simple and easy-to-use interface with sliders and buttons for various image editing options.

## Requirements
- Python 3.x
- Tkinter (for GUI)
- Pillow (Python Imaging Library - for image manipulation)
  
You can install the required dependencies using the following command:

```
pip install pillow

```

## Installation

1. Clone this repository to your local machine:
```
git clone https://github.com/maha-veer/python-image-manipulation-project.git

```
2. Navigate to the project directory:
```
   cd python-image-manipulation-project
```
3. Run the application:
```
python main.py
```

Make sure that you have an image file ready to be opened and edited.

## How to Use
1. Open an Image:
  Click the File menu and select Open to choose an image from your local machine.
2. Edit the Image:
  Use the buttons provided for different editing options:
      -Rotate: Rotate the image by dragging the slider.
      -Blur: Adjust the blur effect using the slider.
      -rightness: Increase or decrease brightness using the slider.
      -Border: Add a border to the image.
      -Flip Left-Right: Flip the image horizontally.
      -Flip Top-Bottom: Flip the image vertically.
      -Contrast: Adjust the contrast using the slider.
3. Save the Edited Image:
  -Click the Save option under the File menu to save your edited image.
4. Exit
  -Close the application using the Exit option from the File menu or the exit button.
## Code Structure
-Main Python File (main.py):
    -The main code for the editor which handles GUI creation, image editing functions, and event handling.
-Image Editing Functions:
    -Functions for rotating, blurring, adjusting brightness, adding borders, flipping, and adjusting contrast of the image.
-Tkinter GUI:
    -The GUI layout is created using Tkinter, with buttons and sliders to allow users to control image editing functions.
## Author
This photo editor was designed and developed by Mahaveer.
## License
This project is open-source and available under the MIT License. Feel free to use and modify it as per your needs.
## Acknowledgements
-The project uses Pillow for image processing.
-Tkinter is used for building the graphical user interface.

For any issues or suggestions, feel free to open an issue in the repository.



