import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

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
