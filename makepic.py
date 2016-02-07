import math

def makepic():
    pic = "P3\n500 500 255\n"
    for x in range(500):
        for y in range(500):
            red = (x*4) % 256
            green = (y*4) % 256
            blue = 255
            pic += "%d %d %d "% (red, green, blue)
    f = open("pic.pbm", "w")
    f.write(pic)

makepic()
