import numpy
import pyglet

# Groesse des zu erzeugenden Bildes
datawidth = 255
dataheight = 100

# RGBA-Format hat 4 Kanaele je 1 Byte
format_size = 4
bytes_per_channel = 1

# Array mit RGBA-Werten fuellen, die einen Verlauf von Rottoenen ergeben
data = numpy.zeros((datawidth * dataheight, format_size), dtype=int)
for i in range(datawidth):
    for j in range(dataheight):
        # Werte im R-Kanal setzen
        data[j * datawidth + i, 0] = i
        # Werte im A-Kanal alle auf 255 setzen
        data[j * datawidth + i, 3] = 255

# Flatten
data.shape = -1

# Konvertierung in Werte, die pyglet erwartet
tex_data = (pyglet.gl.GLubyte * data.size)(*data.astype('uint8'))

# Bild erzeugen und an Sprite uebergeben
myimg = pyglet.image.ImageData(datawidth, dataheight, "RGBA", tex_data,pitch=datawidth * format_size * bytes_per_channel)
myspr = pyglet.sprite.Sprite(myimg)

# Daten zum erzeugten Bild
imgdata = myimg.get_image_data()
mywidth = imgdata.width
myheight = imgdata.height
print("Das erzeugte Bild ist ", mywidth, "x", myheight, "Pixel gross")

# Fenster und seine Eigenschaften definieren
window = pyglet.window.Window(width=400, height=400, resizable=True, caption='Beispiel zum Anzeigen von Images')


# Funktion die beim Zeichnen des Fensters ausgefuehrt wird
@window.event
def on_draw():
    window.clear()
    myspr.draw()


# Start der Ausfuehrung des Fensters
pyglet.app.run()