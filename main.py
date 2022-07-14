from ursina import *
import random
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
sky_tex = load_texture('Misc/sky.jpg')
DirtBlockTexture = load_texture('Misc/source/Grass_Block_TEX.png')
#def random_block():
    #StoneBlockTexture = load_texture('Misc/stone.png')
    #MagmaBlockTexture = load_texture('Misc/magma.jpg')
    #BlockList = [DirtBlockTexture, StoneBlockTexture, MagmaBlockTexture]
    #random.choice(BlockList)


class Voxel(Button):
    def __init__(self,position = (0,0,0)):
        super().__init__(
            parent = scene, 
            model = 'Misc/source/Grass_Block.obj',
            origin_y = 0.5,
            position = position,
            texture =  DirtBlockTexture,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.lime,
            scale = 0.5,
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)

            
            if key == 'right mouse down':
                destroy(self)
        
class sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_tex,
            scale = 150,
            position = (0,0,0),
            double_sided = True,
        )

for z in range(30):
    for x in range(30):
        voxel = Voxel(position = (z,0,x))
player = FirstPersonController()
sky = sky()
app.run()