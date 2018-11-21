import pyglet
import numpy
import sys


def load_img_into_array(path):
    global img_height
    global img_width

    img = pyglet.image.load(path)
    imgdata = img.get_image_data()
    img_width = imgdata.width
    img_height = imgdata.height
    img_array = numpy.full((img_height, img_width, 3), 0)
    px_str = imgdata.get_data('RGB', img_width * 3)

    i = 0
    for row in range(0, img_height):
        for column in range(0, img_width):
            img_array[row][column][0] = px_str[i]
            img_array[row][column][1] = px_str[i + 1]
            img_array[row][column][2] = px_str[i + 2]
            i = i + 3
    return img_array


def dither_img(img_array, dither_array, num_colour):
    new_image_array = numpy.full((img_height, img_width), 0)
    for row in range(0, img_height, 3):
        for column in range(0, img_width, 3):
            for dither_row in range(0, 3):
                for dither_column in range(0, 3):
                    if img_array[row][column][num_colour] / 26 > dither_array[dither_row][dither_column]:
                        new_image_array[row][column] = 1
    return new_image_array


#####################################START

img_path = 'lena.png'#sys.argv[1]
img_array = load_img_into_array(img_path)
dither_array = numpy.array([[0, 7, 3], [6, 5, 2], [4, 1, 8]])
dithered_red = dither_img(img_array, dither_array, 0)
dithered_green = dither_img(img_array, dither_array, 1)
dithered_blue = dither_img(img_array, dither_array, 2)

# create array
ord_array = numpy.full((img_height, img_width, 3), 0)

# put the arrays into ord_array
for row in range(0, img_height):
    for column in range(0, img_width):
        ord_array[row][column][0] = dithered_red[row][column] * 255
        ord_array[row][column][1] = dithered_green[row][column] * 255
        ord_array[row][column][2] = dithered_blue[row][column] * 255

ord_array.shape = -1
img_data = (pyglet.gl.GLubyte * ord_array.size)(*ord_array.astype('uint8'))
rendered_img = pyglet.image.ImageData(img_width, img_height, "RGB", img_data, pitch=img_width * 3)
myspr = pyglet.sprite.Sprite(rendered_img)

window = pyglet.window.Window(width=400, height=400, resizable=True, caption='Beispiel zum Anzeigen von Images')


# Funktion die beim Zeichnen des Fensters ausgefuehrt wird
@window.event
def on_draw():
    window.clear()
    myspr.draw()


# Start der Ausfuehrung des Fensters
pyglet.app.run()
