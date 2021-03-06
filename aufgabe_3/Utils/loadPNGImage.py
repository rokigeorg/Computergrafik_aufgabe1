import pyglet
from pyglet.image.codecs.png import PNGImageDecoder

#Farben definieren und in Variablen ablegen
BACKGROUND_COLOR = (0.9, 0.9, 0.9, 1)
DRAWING_COLOR_1 = (1, 0, 0)
DRAWING_COLOR_2 = (0,0.5,0.5)

#Fenster und seine Eigenschaften definieren
window = pyglet.window.Window(width=400,height=400,resizable=True,caption='Beispiel zum Zeichnen')

#Bilddatei einlesen und zum Anzeigen ablegen
myimg = pyglet.image.load('m.png', decoder=PNGImageDecoder())
myspr = pyglet.sprite.Sprite(myimg)

#Daten zum Bild
imgdata = myimg.get_image_data()
mywidth = imgdata.width
myheight = imgdata.height
print("Das Bild ist ", mywidth, "x", myheight, "Pixel gross")

for i in range(0, 15):
   #Auf Pixel im Bild zugreifen
   pixstr = imgdata.get_data('RGB',mywidth * 3)
   r = pixstr[i]
   g = pixstr[i+1]
   b = pixstr[i+2]
   print("Das Pixel an der Stelle (",i,",0) hat die Farbe (", r, ",", g, ",", b, ").")

#Funktion die beim Zeichnen des Fensters ausgefuehrt wird
@window.event
def on_draw():
   window.clear()
   myspr.draw()

   #zusaetzlich eine Strecke ins Bild zeichnen
   pyglet.graphics.draw(2, pyglet.gl.GL_LINES,('v2i', (110, 100, 310, 300)))

#Start der Ausfuehrung des Fensters
pyglet.app.run()
