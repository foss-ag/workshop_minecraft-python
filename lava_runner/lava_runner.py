import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

###########################################
# random parcour generator

###########################################

while(True):
    # check if player is standing on an ice block
    (x, y, z) = mc.player.getTilePos()
    block = mc.getBlock((x, y-1, z))
    # remove ice block a second after the player entered the block
    if block == 79:
        sleep(1)
        mc.setBlock((x, y-1, z), 0)
