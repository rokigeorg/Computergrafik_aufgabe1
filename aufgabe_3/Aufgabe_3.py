from typing import List, Any

import pyglet
import numpy as np
import cv2

# Fenster und seine Eigenschaften definieren
from pyglet.gl import GLubyte

window = pyglet.window.Window(width=400, height=400, resizable=True, caption='Beispiel zum Zeichnen')


class PocessImage():
    def __init__(self, imgPath):
        self.image_path = imgPath
        self.image = self.loadImg()
        self.data = self.loadImgData()
        self.chRed = self.loadChannel("r")
        self.chGreen = self.loadChannel("g")
        self.chBlue = self.loadChannel("b")

    def loadImgData(self):
        return self.image.get_image_data()

    def loadImg(self):
        return pyglet.image.load(self.image_path)

    def loadChannel(self, channel):
        imgdata = self.data
        pixstr = imgdata.get_data('RGB', self.data.width * 3)
        if channel == "r":
            lst = list()
            for i in range(0, self.data.width * 3, 3):
                lst.append(pixstr[i])
            return self.createMatrix(lst)
        elif channel == "g":
            lst = list()
            for i in range(1, self.data.width * 3, 3):
                lst.append(pixstr[i])
            return self.createMatrix(lst)
        elif channel == "b":
            lst = list()
            for i in range(2, self.data.width * 3, 3):
                lst.append(pixstr[i])
            return self.createMatrix(lst)

    def createMatrix(self, lst):
        mtx = list()
        for j in range(0, self.data.height):
            a = list()
            for i in range(0, self.data.width):
                a.append(lst[i])
            mtx.append(a)

        return np.matrix(mtx)

    def getPixel(self, x, y, ch):
        if ch == "r":
            return self.chRed.item(x, y)
        elif ch == "g":
            return self.chGreen.item(x, y)
        else:
            return self.chBlue.item(x, y)

    def faltung(self, filter_signal, radius, channel="r"):
        r = radius
        h = filter_signal

        iaus = np.zeros((self.data.width - 1, self.data.height - 1))
        s = np.zeros(self.data.width - 1)
        # print(s)

        for y in range(r, self.data.height - 1 - r):
            for x in range(0, self.data.width - 1):
                s[x] = 0
                for v in range(0, r):
                    s[x] = s[x] + h[v] * self.getPixel(x, y - v, channel)
            for x in range(0, self.data.width - 1):
                for u in range(0, r):
                    iaus[x][y] = iaus[x][y] + h[u] * s[x - u]
        return iaus


class GuiImage():
    def __init__(self, width, height, format, rdata, gdata, bdata):
        self.height = height
        self.width = width
        self.format = format
        self.red = rdata
        self.green = gdata
        self.blue = bdata
        self.format_size = 4
        self.data = self.createRMatrix()
        self.bytes_per_channel = 1


    def createRMatrix(self):
        data = np.zeros((self.width * self.height, self.format_size), dtype=int)

        for i in range(self.width - 1):
            for j in range(self.height - 1):
                # Werte im R-Kanal setzen
                data[j * self.height + i, 0] = self.red[i][j]
                # Werte im G-Kanal setzen
                data[j * self.height + i, 0] = self.green[i][j]
                # Werte im B-Kanal setzen
                data[j * self.height + i, 0] = self.blue[i][j]
                # Werte im A-Kanal alle auf 255 setzen
                data[j * self.width + i, 3] = 255

        return data

    def createRGBImage(self):
        # Flatten
        self.data.shape = -1

        # Konvertierung in Werte, die pyglet erwartet
        tex_data = (pyglet.gl.GLubyte * self.data.size)(*self.data.astype('uint8'))
        myimg = pyglet.image.ImageData(self.width, self.height, "RGBA", tex_data,
                                       pitch=self.width * self.format_size * self.bytes_per_channel)
        return myimg

    def getImg(self):
        return self.createRGBImage()


'''           
    def createRgbA(self):
        arr = list()  # type: List[Any]
        onEnd = False
        i = 0
        while onEnd:
            arr[i] = self.red[i]
            arr[i + 1] = self.red[i]
            arr[i + 1] = self.red[i]
            i = i + 3
            if i == self.width * 3:
                onEnd = True
        return arr

    def createRgbArray(self):
        l = list()
        for i in range(0, self.width * 3):
            if i % 3 == 0:
                tmp = self.blue[i]
            elif i % 2 == 0:
                tmp = self.green[i]
            else:
                tmp = self.red[i]
            l.append(tmp)
        self.rgbData = l
'''


def gKernel(r):
    r = float(r) / 2
    x = np.arange(r * -1, r, 1)  # x from -r to r in steps of 0.1
    return 1 / np.sqrt(2 * np.pi) * np.exp(-x ** 2 / 2.)


def start_image_processing():
    r = int(input("Geben sie filter radius ein: "))
    # create gauss kernel
    gauss = gKernel(r)
    print(gauss)
    pimg = PocessImage('lena.png')
    pimg.getPixel(1, 1, "r")

    # falung der beiden signale
    mRed = pimg.faltung(gauss, r, "r")
    mGreen = pimg.faltung(gauss, r, "g")
    mBlue = pimg.faltung(gauss, r, "b")

    return mRed, mGreen, mBlue


# Funktion die beim Zeichnen des Fensters ausgefuehrt wird
@window.event
def on_draw():
    window.clear()

    p = GuiImage(512, 512, "RGB", mRed, mGreen, mBlue)
    p.createRMatrix()
    img = p.getImg()
    img.blit(0, 0)


if __name__ == "__main__":
    print("******* Gauss image filter ***** ")

    mRed, mGreen, mBlue = start_image_processing()

    # x = np.array([2, 3, 4, 5])
    # print(x)

    pyglet.app.run()
