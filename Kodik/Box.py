from ursina import *

app = Ursina()
window.color = color.black

Light(type='ambient',  color=(0.5, 0.5, 0.5, 1))
Light(type='directional',  color=(0.5, 0.5, 0.5, 1), direction=(1, 1, 1))

cube = Entity(model='cube', rotation=(-15, 0, 0), position=(0, 0, 0), scale=4, color=color.orange)

def update():
    cube.rotation_y += time.dt * 100
    cube.x += held_keys['d'] * time.dt * 5
    cube.x -= held_keys['a'] * time.dt * 5

app.run()