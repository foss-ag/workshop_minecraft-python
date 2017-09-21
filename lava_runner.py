import mcpi.minecraft as minecraft
from time import sleep

mc = minecraft.Minecraft.create()

# initialise are for lava runner game
def initialise():
    # get players current position
    (x, y, z) = mc.player.getTilePos()
    # area to flatten around players position
    area_flat_ground = [(x_, y_, z_) for x_ in range(x-11, x+25) for y_ in range(y-10, y) for z_ in range(z-11, z+11)]
    area_flat_air = [(x_, y_, z_) for x_ in range(x-11, x+25) for y_ in range(y, y+10) for z_ in range(z-11, z+11)]
    # area to fill with lava
    area_lava = [(x_, y_, z_) for x_ in range(x+1, x+15) for y_ in range(y-4, y) for z_ in range(z-10, z+10)]
    
    # flatten area and fill with lava
    map(lambda pos: mc.setBlock(pos, 2), area_flat_ground)
    map(lambda pos: mc.setBlock(pos, 0), area_flat_air)
    map(lambda pos: mc.setBlock(pos, 10), area_lava)
    
    # mark start position
    mc.setBlock((x, y-1, z), 57)

#generate random parcour
def random_parcour():
    None

initialise()
random_parcour()

while(True):
    # check if player is standing on an ice block
    (x, y, z) = mc.player.getTilePos()
    block = mc.getBlock((x, y-1, z))
    # remove ice block a second after the player entered the block
    if block == 79:
        sleep(1)
        mc.setBlock((x, y-1, z), 0)