import pyglet
import time
import sys

window = pyglet.window.Window(width=600, height=600, resizable=False, caption='Raster')

# *******
# Globals
# *******

drawing_color1 = (1, 1, 1)
drawing_color2 = (0, 0.5, 0.5)

mX0 = 0
mY0 = 0
mX1 = 0
mY1 = 0


# *******
# Models
# *******

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Strecke():

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class Pixel():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        x_internal = self.x * 100
        y_internal = self.y * 100
        self.p0 = Point(x_internal, y_internal)
        self.p1 = Point(x_internal + 100, y_internal)
        self.p2 = Point(x_internal + 100, y_internal + 100)
        self.p3 = Point(x_internal, y_internal + 100)
        # self.inlX= x +100 if x > 0 else self.inlX= x
        # self.inlY= y +100 if y > 0 else self.inlY= y

    # 0+ -
    def draw(self):
        # Zeichenfarbe setzen
        pyglet.gl.glColor3f(*drawing_color2)
        # ausgefuelltes Polygon (Viereck) zeichnen
        #    pyglet.graphics.draw(4, pyglet.gl.GL_POLYGON, ('v2i', (100, 100, 300, 300, 200, 350, 100, 300)))
        pyglet.graphics.draw(4, pyglet.gl.GL_POLYGON, (
            'v2i', (self.p0.x, self.p0.y, self.p1.x, self.p1.y, self.p2.x, self.p2.y, self.p3.x, self.p3.y)))


# *******
# Function
# *******

def lineDraw2(p1, p2):
    # create a line context
    pyglet.gl.glColor3f(*drawing_color1)
    pyglet.graphics.glBegin(pyglet.graphics.GL_LINES)
    # create a line, x,y,z
    pyglet.graphics.glVertex3f(p1.x, p1.y, 0)
    pyglet.graphics.glVertex3f(p2.x, p2.y, 0)
    pyglet.graphics.glEnd()


def rasterDraw():
    s1 = Strecke(Point(100, 0), Point(100, 600))
    s2 = Strecke(Point(200, 0), Point(200, 600))
    s3 = Strecke(Point(300, 0), Point(300, 600))
    s4 = Strecke(Point(400, 0), Point(400, 600))
    s5 = Strecke(Point(500, 0), Point(500, 600))
    h1 = Strecke(Point(0, 100), Point(600, 100))
    h2 = Strecke(Point(0, 200), Point(600, 200))
    h3 = Strecke(Point(0, 300), Point(600, 300))
    h4 = Strecke(Point(0, 400), Point(600, 400))
    h5 = Strecke(Point(0, 500), Point(600, 500))

    arr = [s1, s2, s3, s4, s5, h1, h2, h3, h4, h5]

    for item in arr:
        # create a line context
        pyglet.graphics.glBegin(pyglet.graphics.GL_LINES)
        # create a line, x,y,z
        pyglet.graphics.glVertex3f(item.p1.x, item.p1.y, 0)
        pyglet.graphics.glVertex3f(item.p2.x, item.p2.y, 0)
        pyglet.graphics.glEnd()


class Alg():

    def __init__(self):
        self.sPxl = Pixel(0, 0)
        self.ePxl = Pixel(0, 0)

    def rasterAlg(self, x0, y0, x1, y1):
        sPxl = self.sPxl = Pixel(x0, y0)
        ePxl = self.ePxl = Pixel(x1, y1)
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

        y = sPxl.y
        # d = self.gFkt(sPxl.x + 1, y + 0.5)
        d = (2 * (y0 - y1) * (x0 + 1)) + ((x1 - x0) * ((2 * y0) + 1)) + (((2 * x0) * y1) - ((2 * x1) * y0))
        for x in range(sPxl.x, (ePxl.x + 1)):
            Pixel(x, y).draw()
            print(d)
            if d < 0:
                y = y + 1
                # d = d + (y0 - y1) + (x1 - x0)
                d = (d + ((2 * (y0 - y1)) + (2 * (x1 - x0))))  # (y0 - y1) + (x1 - x0)
            else:
                # d = d + (y0 - y1)
                d = (d + ((2 * (y0 - y1))))

    def gFkt(self, x, y):
        x0 = self.x0
        y0 = self.y0
        x1 = self.x1
        y1 = self.y1
        return (x * (y0 - y1)) + (y * (x0 - x1)) + ((x0 * y1) - (x1 * y0))

    def rasterAlg2(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

        d = (2 * (y1 - y0)) - (x1 - x0)
        do = (2 * (y1 - y0))
        ndo = 2 * ((y1 - y0) - (x1 - x0))
        y = y0
        Pixel(x0, y0).draw()
        for x in range((x0 + 1), (x1 + 1)):
            if d <= 0:
                d = d + do
            else:
                d = d + ndo
                y = y + 1
            Pixel(x, y).draw()


# *******
# MAIN FKT
# *******

@window.event
def on_draw():
    window.clear()
    rasterDraw()

    a = Alg()
    # a.rasterAlg(0,0,5,3)
    a.rasterAlg2(mX0, mY0, mX1, mY1)

    # TODO end fkt 0,0 zu 5,3
    lineDraw2(Point(mX0*100, mY0*100), Point(mX1*100, mY1*100+50))


if __name__ == "__main__":
    arr = sys.argv[1:]
    if not arr:
        print("Error!!! No args passed!")
        exit(-1)

    mX0 = int(arr[0])
    mY0 = int(arr[1])
    mX1 = int(arr[2])
    mY1 = int(arr[3])

    if (mX0 < 0 or mX0 > 5 or mX1 < 0 or mX1 > 5 or mY0 < 0 or mY0 > 5 or mY1 < 0 or mY1 > 5):
        print("Error!!! Coordinates are shit!")
        print("The programm args are the started point (x0, y0) and endpoint (x1, y1). \nPossible coordinats are for the x-achses {0:5} and y-achses {0:5}.")
        exit(-1)

    if mX1 < mX0:
        tmpX = mX0
        tmpY = mY0

        mX0 = mX1
        mY0 = mY1
        mX1 = tmpX
        mY1 = tmpY

    pyglet.app.run()
