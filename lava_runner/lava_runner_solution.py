import mcpi.minecraft as minecraft
import random

mc = minecraft.Minecraft.create()

###########################################
# random parcour generator
# Version 1
(x, y, z) = mc.player.getTilePos()
lower_bound = y
for _ in range(15):
    x = random.randint(x-2, x+2)
    y = max(random.randint(y-2, y+1), lower_bound)
    z += 1
    mc.setBlock((x, y, z), 79)

# Version 2
(x, y, z) = mc.player.getTilePos()
for i in range(15):
    x2 = random.randint(x-2, x+2)
    y2 = random.randint(y-2, y+1)
    if y2 < y:
        y2 = y
    z2 = z+1
    mc.setBlock((x2, y2, z2), 79)
    (x, y ,z) = (x2, y2, z2)
###########################################

while(True):
    # check if player is standing on an ice block
    (x, y, z) = mc.player.getTilePos()
    block = mc.getBlock((x, y-1, z))
    # remove ice block a second after the player entered the block
    if block == 79:
        sleep(1)
        mc.setBlock((x, y-1, z), 0)
