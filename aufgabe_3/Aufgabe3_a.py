import numpy as np
from PIL import Image
import pyglet

window = pyglet.window.Window(width=512, height=512, resizable=True, caption='Lena Gauss gefiltert!')

# Groesse des zu erzeugenden Bildes
global datawidth
global dataheight

# RGBA-Format hat 4 Kanaele je 1 Byte
format_size = 4
bytes_per_channel = 1


def gKernel(r):
    r = float(r) / 2
    x = np.arange(r * -1, r, 1)  # x from -r to r in steps of 0.1
    return 1 / np.sqrt(2 * np.pi) * np.exp(-x ** 2 / 2.)


def setAlpha(data):
    for i in range(datawidth):
        for j in range(dataheight):
            # Werte im R-Kanal setzen
            # Werte im A-Kanal alle auf 255 setzen
            data[j * datawidth + i, 3] = 255
    return data


def faltung2(matrix, filter_signal, radius, width, height):
    r = radius
    h = filter_signal

    iaus = np.zeros((width * height, format_size), dtype=int)
    iaus = setAlpha(iaus)  # set Alpha channel to 255
    for ch in range(0, 3):
        s = np.zeros(width - 1)

        for y in range(r, height - 1 - r):
            for x in range(0, width - 1):
                s[x] = 0
                for v in range(0, r):
                    s[x] = s[x] + h[v] * matrix[x][y - v][ch]
            for x in range(0, width - 1):
                for u in range(0, r):
                    iaus[x * width + y, ch] = int(iaus[x * width + y, ch] + h[u] * s[x - u])
    return iaus


# Funktion die beim Zeichnen des Fensters ausgefuehrt wird
@window.event
def on_draw():
    window.clear()
    myimg.blit(0, 0)

# HERE starts the main programm
if __name__ == "__main__":
    print("******* Gauss image filter ***** ")

    r = int(input("Geben sie filter radius ein: "))
    # create gauss kernel
    gauss = gKernel(r)
    print(gauss)
    img = Image.open('lena.png')
    datawidth = img.width
    dataheight = img.height
    # matrix = loadImageAsMatrix(img)
    matrix = np.array(img)  # 512x512x4 array

    fdata = faltung2(matrix, gauss, r, datawidth, dataheight)
    fdata.shape = -1
    # Konvertierung in Werte, die pyglet erwartet
    tex_data = (pyglet.gl.GLubyte * fdata.size)(*fdata.astype('uint8'))
    myimg = pyglet.image.ImageData(datawidth, dataheight, "RGBA", tex_data,
                                   pitch=datawidth * format_size * bytes_per_channel)

    pyglet.app.run()
