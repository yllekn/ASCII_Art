# I implemented this "ASCII Art" project from a blog post online
# SOURCE: https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/
# The picture prints to terminal; shrink terminal font to the smallest size & expand terminal window to largest size to see picture

from PIL import Image
import numpy as np
import os

def main():
    
    # Open img
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(THIS_FOLDER, 'rm.jpg')
    im = Image.open(file_path)
    # im = Image.open("rm.jpg")
    width, height = im.size
    print("Successfully loaded image!")
    print("Image size:", width, "x", height)

    # Load img into array & print pixel RGB values (tuples)
    arr = np.array(im)
    print(width, height)
    for h in range(height):
        # print("[", sep="", end="")
        for w in range(width): 

            # Map RGB values to brightness
            # Average
            lum = round((int(arr[h, w, 0]) + int(arr[h, w, 1]) + int(arr[h, w, 2])) / 3)
            
            # TODO: Luminosity
            

            lum_inv = 255 - lum - 1
            # print(lum)

            # Map 255 brightnesses to 65 ASCII characters
            # Conversion factor = 1 / (255/65) 
            chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
            lum = int(round(lum / (255/65))) - 1    # map to 65

            # INVERT PIXEL BRIGHTNESSES (uncomment line below to activate)
            # lum = int(round(lum_inv / (255/65))) - 1    # map to 65

            # print(chars[lum], end="")
            # print(matrix)
            if w != width - 1:
                print(chars[lum], end="")
                print(chars[lum], end="")
            else:
                print(chars[lum], end="")
                print(chars[lum])

            # lum = (0.2126 * arr[h, w, 0]) + (0.7252 * arr[h, w, 1]) + (0.0722 * arr[h, w, 2])


        # DEBUG PRINT STATEMENTS
        #     if w != width - 1:
        #         print("(", arr[h, w, 0], ", ", arr[h, w, 1], ", ", arr[h, w, 2], "), ", sep="", end="")
        #     else:
        #         print("(", arr[h, w, 0], ", ", arr[h, w, 1], ", ", arr[h, w, 2], ")", sep="", end="")
        # if h != height - 1: 
        #     print("],")
        # else: 
        #     print("]")
    # print("]")


if __name__ == "__main__":
    main()