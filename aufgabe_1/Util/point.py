import pyglet

window = pyglet.window.Window(600, 600)


@window.event
def on_draw():
    window.clear()
    pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                         ('v2i', (10, 15))
                         )


if __name__ == "__main__":
    pyglet.app.run()
