import numpy as np
from PIL import Image
import sys
import face_recognition

# ASCII characters ranging from lightest (1: ".") to darkest (12: "@")
ascii_chars = {
    1: ".", 
    2: ",", 
    3: "-", 
    4: "~", 
    5: ":", 
    6: ";", 
    7: "=", 
    8: "!", 
    9: "*", 
    10: "#", 
    11: "$", 
    12: "@"
}

def main():
    width = 100
    if len(sys.argv) > 3:                   # Can take a minimum of 2 and maximum of 3 args (including "project.py" as arg 1)
        sys.exit("Too many command-line arguments.")
    if len(sys.argv) < 2:                   
        sys.exit("Too little command-line arguments.")
    try:
        image = face_recognition.load_image_file(sys.argv[1])
        face_locations = face_recognition.face_locations(image)
        if len(face_locations) == 0 or  len(face_locations) > 1:
            raise NameError()
        if len(sys.argv) == 3:
            width = int(sys.argv[2])
            if width < 30:           # Width provided must be atleast 30px
                raise ValueError()
    except NameError:
        sys.exit("Image needs only 1 face. Image provided has no faces or more than 1 face.")
    except FileNotFoundError:
        sys.exit("Command-line argument is not a correct image label and/or extension.")
    except ValueError:
        sys.exit("Command-line argument is not a correct integer value for the width. Must be an int >=30")

    top, right, bottom, left = face_locations[0]

    try:
        face_image = image[top-40:bottom+40, left-60:right+60]  # Locate face and resize image to preserve original ratio for viewing in terminal
        pil_image = Image.fromarray(face_image)
    except ValueError:
        face_image = image[top:bottom, left:right]              # Or don't resize, if have run out of pixels
        pil_image = Image.fromarray(face_image)

    pil_image.thumbnail((100,100))
    pil_image = pil_image.resize((width, width // 2))

    grayscale_image = pil_image.convert("L")                    # Convert resized color image to greyscale
    grayscale_image_as_array = np.asarray(grayscale_image)      # Convert greyscale image to a width x length 2D array 
    scaled_image = modify_array(grayscale_image_as_array)       
    print_ASCII_to_terminal(scaled_image)                       


# Take an RGB value ranging from 0-255 and return a scaled value following a 1-12 scale
def convert_RGB_to_12_scale(rgb_value):
    match rgb_value:
        case num if num in range(0,20):
            return 1
        case num if num in range(20,40):
            return 2
        case num if num in range(40,60):
            return 3
        case num if num in range(60,80):
            return 4
        case num if num in range(80,100):
            return 5
        case num if num in range(100,120):
            return 6
        case num if num in range(120,140):
            return 7
        case num if num in range(140,160):
            return 8
        case num if num in range(160,180):
            return 9
        case num if num in range(180,200):
            return 10
        case num if num in range(200,220):
            return 11
        case num if num in range(220,256):
            return 12
        case _:
            return -1
        
# Return scaled array having values ranging from 1-12, based on pixel darkness
def modify_array(grayscale_array):
    new_array = []
    for r in range(len(grayscale_array)):
        new_array.append([])
        for c in range(len(grayscale_array[r])):
            new_array[r].append(convert_RGB_to_12_scale(grayscale_array[r][c]))
    return new_array

# Output ASCII image to terminal
def print_ASCII_to_terminal(grayscale_array):
    for r in range(len(grayscale_array)):
        for c in range(len(grayscale_array[r])):
            try:
                print(ascii_chars[grayscale_array[r][c]], end="")
            except KeyError:
                print(grayscale_array[r][c])
                sys.exit()
        print()

if __name__ == "__main__":
    main()