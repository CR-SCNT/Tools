import sys
from PIL import Image

batch = sys.argv[1]


if batch != 0 or batch != 1:
    raise("Wrong argument")

if batch == 0:
    image = Image.open("pic.jpg")
    pixels = image.load()
    width, height = image.size
    R, G, B = pixels[width/2, height/2]
    print("pic.jpg -> (", R, " ", G, " ", B, ")"  )
elif batch == 1:
    if sys.argv.length() <= 2:
        number = int(input("Please enter the number of files you want process (from 1 to 8)"))
    else:
        number = sys.argv[2]
    temps = ["1", "2", "3", "4", "5", "6", "7", "8"]
    for i in range(number):
        filename = "pic" + temps[i] + ".jpg"
        image = Image.opne(filename)
        pixels = image.load()
        width, height = image.size
        R, G, B = pixels[width/2, height/2]
        print( filename, " -> (", R, " ", G, " ", B, ")"  )
        
