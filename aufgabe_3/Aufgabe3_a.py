import numpy as np
import pyglet

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


def gKernel(r):
    r = float(r) / 2
    x = np.arange(r * -1, r, 1)  # x from -r to r in steps of 0.1
    return 1 / np.sqrt(2 * np.pi) * np.exp(-x ** 2 / 2.)


# Funktion die beim Zeichnen des Fensters ausgefuehrt wird
@window.event
def on_draw():
    window.clear()


if __name__ == "__main__":
    print("******* Gauss image filter ***** ")

    r = int(input("Geben sie filter radius ein: "))
    # create gauss kernel
    gauss = gKernel(r)
    print(gauss)
    pimg = PocessImage('lena.png')

    pyglet.app.run()
