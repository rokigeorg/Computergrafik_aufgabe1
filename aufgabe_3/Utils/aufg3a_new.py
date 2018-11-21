import numpy as np
from PIL import Image
import pyglet

window = pyglet.window.Window(width=512, height=512, resizable=True, caption='Lena Gauss gefiltert!')


img = Image.open('lena.png')
data = np.array(img) # 512x512x4 array
print(data[15][0][0])



# Flatten
data.shape = -1

# Konvertierung in Werte, die pyglet erwartet
tex_data = (pyglet.gl.GLubyte * data.size)(*data.astype('uint8'))

# Bild erzeugen und an Sprite uebergeben
myimg = pyglet.image.ImageData(512, 512, "RGB", tex_data,pitch=512 * 3 * 1)


# Funktion die beim Zeichnen des Fensters ausgefuehrt wird
@window.event
def on_draw():
    window.clear()
    myimg.blit(0, 0)

pyglet.app.run()
