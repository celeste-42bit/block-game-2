from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import floor
from perlin_noise import PerlinNoise

app = Ursina()

Sky(texture=load_texture("sky_sunset.jpg"))

generator_settings = [42069, 1, 20, 10]  # format [seed, octaves, frequency, amplitude]
terrain_size = 50

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
    return color.rgb(red, green, blue)

terrain = Entity(model = None, collider = None)

heightmap = PerlinNoise(octaves = generator_settings[1], seed = generator_settings[0])

for n in range(terrain_size * terrain_size):
    block = Entity(model = 'cube', color = random_color())
    block.x = floor(n/terrain_size)
    block.z = floor(n%terrain_size)
    block.y = floor((heightmap([block.x / generator_settings[2], block.z / generator_settings[2]])) * generator_settings[3])
    block.parent = terrain

terrain.combine(auto_destroy = True)  # destroying children (for now) because of visual glitch. Deactivate after fix.
terrain.texture = 'grass'
terrain.collider = 'mesh'

player = FirstPersonController()
player.X = 5
player.Z = 5
player.Y = 5

app.run()