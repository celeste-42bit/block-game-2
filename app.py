from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()
window.color = color.rgba(200, 200, 255, 1)
Sky(texture=load_texture("sky_sunset.jpg"))

def input(key):
    match key:

        case 'escape':
            print('Code 0 (Ok)')
            application.quit()

        case 'x':
            print('Action button!')

def update():
    pass

def random_color():
    red = random.Random().random() * 255
    green = random.Random().random() * 255
    blue = random.Random().random() * 255
    return color.rgba(red, green, blue)

terrain = Entity(model = None, collider = None)

terrain_size = 50
for i in range(terrain_size * terrain_size):
    block = Entity(model = 'cube', color = random_color(), texture = 'grass')
    block.x = i/terrain_size
    block.z = i%terrain_size
    block.y = 0
    block.parent = terrain

terrain.combine(auto_destroy = True)  # do not destroy the children after combine
terrain.collider = 'mesh'

player = FirstPersonController()
player.X = 5
player.Z = 5
player.Y = 5

app.run()