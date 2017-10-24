import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep

mc = minecraft.Minecraft.create()

# define boundary for x and z coordinates
x_boundary = 0
z_boundary = 0

##########################################################
# random parcour generator
def generate_parcour(x, y, z):
    # your code here
    
    mc.setBlocks(x - 2, y - 1, z - 1, x + 1, y - 1, z + 1, block.GOLD_BLOCK)
##########################################################

# arena dimensions
arena_width = 30
arena_height = 25
# get player position and check if player is standing on an obsidian block
(x, y, z) = mc.player.getTilePos()
if mc.getBlock(x, y-1, z) == 49:
    # define arena boundaries
    x_boundary = x-1 + arena_width - 4
    z_boundary = z-1 + arena_width - 4
    # generate random parcour
    generate_parcour(x, y-1, z)

    while True:
        (x_, y_, z_) = mc.player.getTilePos()
        # if player has fallen into the lava, respawn and generate new random parcour
        if mc.getBlock(x_, y_-1, z_) == 247:
            # remove old generated path
            mc.setBlocks(x, y-1, z, x+arena_width-4, y+arena_height-10, z+arena_width-4, block.AIR)
            # set start platform
            mc.setBlocks(x-1, y-1, z-1, x+2, y-1, z+2, block.STONE)
            mc.setBlock((x, y-1, z), block.OBSIDIAN)
            # teleport player
            mc.player.setPos(x+1, y+2, z)
            # generate new random parcour
            generate_parcour(x, y-1, z)
        elif mc.getBlock(x_, y_-1, z_) == 79:
                sleep(1.5)
                mc.setBlock(x_, y_-1, z_, 0)
        # if player has reached the goal, teleport to fancy special place
        elif mc.getBlock(x_, y_-1, z_) == 41:
            mc.player.setPos(x+53, y+1, z+53)
            break
