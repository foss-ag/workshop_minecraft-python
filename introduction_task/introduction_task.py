import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

# flower block ID
flower = 38

# this loop runs forever
while True:
    # get players current position
    (x, y, z) = mc.player.getPos()
    # place flowers at players position
    mc.setBlock(x, y, z, flower)
