import pyglet

# Farben definieren und in Variablen ablegen
BACKGROUND_COLOR = (0.9, 0.9, 0.9, 1)
D_COLOR_1 = (0, 0, 0)
D_COLOR_2 = (0, 0.5, 0.5)

# Fenster und seine Eigenschaften definieren
window = pyglet.window.Window(width=400, height=400, resizable=True, caption='Beispiel zu Transformationen')


def createWorld():
    # 1. Sprite
    pyglet.gl.glVertex2f(100, 100)
    pyglet.gl.glVertex2f(200, 100)
    pyglet.gl.glVertex2f(200, 200)
    pyglet.gl.glVertex2f(100, 200)
    # 2. Sprite
    pyglet.gl.glVertex2f(100, 600)
    pyglet.gl.glVertex2f(200, 600)
    pyglet.gl.glVertex2f(200, 700)
    pyglet.gl.glVertex2f(100, 700)
    # 3. 4. Sprite
    pyglet.gl.glVertex2f(400, 300)
    pyglet.gl.glVertex2f(500, 300)
    pyglet.gl.glVertex2f(500, 500)
    pyglet.gl.glVertex2f(400, 500)
    # 5. 6. Sprite
    pyglet.gl.glVertex2f(400, 700)
    pyglet.gl.glVertex2f(600, 700)
    pyglet.gl.glVertex2f(600, 800)
    pyglet.gl.glVertex2f(400, 800)
    # 7.8. Sprite
    pyglet.gl.glVertex2f(500, 1000)
    pyglet.gl.glVertex2f(700, 1000)
    pyglet.gl.glVertex2f(700, 1100)
    pyglet.gl.glVertex2f(500, 1100)
    # 9.10. Sprite
    pyglet.gl.glVertex2f(700, 400)
    pyglet.gl.glVertex2f(900, 400)
    pyglet.gl.glVertex2f(900, 500)
    pyglet.gl.glVertex2f(700, 500)
    # 11. Sprite
    pyglet.gl.glVertex2f(800, 600)
    pyglet.gl.glVertex2f(900, 600)
    pyglet.gl.glVertex2f(900, 700)
    pyglet.gl.glVertex2f(800, 700)
    # 12. Sprite
    pyglet.gl.glVertex2f(800, 1200)
    pyglet.gl.glVertex2f(900, 1200)
    pyglet.gl.glVertex2f(900, 1300)
    pyglet.gl.glVertex2f(800, 1300)
    # 13. 14. Sprite
    pyglet.gl.glVertex2f(1000, 900)
    pyglet.gl.glVertex2f(1100, 900)
    pyglet.gl.glVertex2f(1100, 1000)
    pyglet.gl.glVertex2f(1000, 1000)

    # 15. Sprite
    pyglet.gl.glVertex2f(900, 1700)
    pyglet.gl.glVertex2f(1000, 1700)
    pyglet.gl.glVertex2f(1000, 1800)
    pyglet.gl.glVertex2f(900, 1800)

    # 16. Sprite
    pyglet.gl.glVertex2f(1100, 1500)
    pyglet.gl.glVertex2f(1200, 1500)
    pyglet.gl.glVertex2f(1200, 1600)
    pyglet.gl.glVertex2f(1100, 1600)

    # 17. Sprite
    pyglet.gl.glVertex2f(1200, 700)
    pyglet.gl.glVertex2f(1300, 700)
    pyglet.gl.glVertex2f(1300, 800)
    pyglet.gl.glVertex2f(1200, 800)

    # 18. Sprite
    pyglet.gl.glVertex2f(1200, 1300)
    pyglet.gl.glVertex2f(1300, 1300)
    pyglet.gl.glVertex2f(1300, 1400)
    pyglet.gl.glVertex2f(1200, 1400)

    # 19. Sprite
    pyglet.gl.glVertex2f(1400, 900)
    pyglet.gl.glVertex2f(1500, 900)
    pyglet.gl.glVertex2f(1500, 1000)
    pyglet.gl.glVertex2f(1400, 1000)
    # 20. Sprite
    pyglet.gl.glVertex2f(1400, 1100)
    pyglet.gl.glVertex2f(1500, 1100)
    pyglet.gl.glVertex2f(1500, 1200)
    pyglet.gl.glVertex2f(1400, 1200)

# Funktion die beim Zeichnen des Fensters ausgefuehrt wird
@window.event
def on_draw():
    # Hintergrundfarbe setzen
    pyglet.gl.glClearColor(*BACKGROUND_COLOR)
    window.clear()

    # Zeichenfarbe setzen
    pyglet.gl.glColor3f(*D_COLOR_1)

    # Transformationsmatrix angeben
    pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)
    # Ausgangspunkt ist die Einheitsmatrix
    pyglet.gl.glLoadIdentity()
    # Verschiebung des Koordinatenursprungs
    pyglet.gl.glTranslatef(100.0, 100.0, 0.0)
    # Drehung um die z-Achse um 45 Grad um aktuellen Koordinatenursprung
   # pyglet.gl.glRotatef(45, 0.0, 0.0, 1.0)
    # Verschiebung des Koordinatenursprungs
   # pyglet.gl.glTranslatef(-100.0, -100.0, 0.0)
    # Achtung: letzte Transformation (Matrix) wird zuerst angewendet!

    # Szene aus zwei Rechtecken
    pyglet.gl.glBegin(pyglet.gl.GL_QUADS)

    #draw the World
    createWorld()


    pyglet.gl.glEnd()


if __name__ == "__main__":
    # Start der Ausfuehrung des Programms
    pyglet.app.run()
