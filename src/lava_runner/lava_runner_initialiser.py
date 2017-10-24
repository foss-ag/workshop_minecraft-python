import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
player_positions = mc.player.getTilePos()

arena_wall_start_position = (player_positions.x, player_positions.y, player_positions.z)
arena_width = 30
arena_height = 25
start_position = (arena_wall_start_position[0] + 1, arena_wall_start_position[1] + 5, arena_wall_start_position[2] + 1)
path_start_position = (start_position[0] + 2, start_position[1] + 1, start_position[2] + 2)

# build arena
mc.setBlocks(arena_wall_start_position[0], arena_wall_start_position[1], arena_wall_start_position[2], arena_wall_start_position[0] + arena_width, arena_wall_start_position[1] + arena_height, arena_wall_start_position[2] + arena_width, block.NETHER_REACTOR_CORE)

# fill arena with air
mc.setBlocks(arena_wall_start_position[0] + 1, arena_wall_start_position[1] + 1, arena_wall_start_position[2] + 1, arena_wall_start_position[0] + arena_width - 2, arena_wall_start_position[1] + arena_height-1, arena_wall_start_position[2] + arena_width - 2, block.AIR)

# set lava
mc.setBlocks(arena_wall_start_position[0] + 1, arena_wall_start_position[1] + 1, arena_wall_start_position[2] + 1, arena_wall_start_position[0] + arena_width - 2, arena_wall_start_position[1] + 2, arena_wall_start_position[2] + arena_width - 2, block.LAVA)

# set start platform
mc.setBlocks(start_position[0], start_position[1], start_position[2], start_position[0] + 3, start_position[1] + 1, start_position[2] + 3, block.STONE)
mc.setBlocks(start_position[0] + 1, start_position[1] + 1, start_position[2] + 1,start_position[0] + 2, start_position[1] + 1, start_position[2] + 2, block.OBSIDIAN)

# teleport player to start position
mc.player.setPos(start_position[0] + 1, start_position[1] + 2, start_position[2] + 1)

# create special place
mc.setBlocks(start_position[0]+48, start_position[1], start_position[2]+48, start_position[0]+62, start_position[1]+12, start_position[2]+62, 246)
mc.setBlocks(start_position[0]+49, start_position[1]+1, start_position[2]+49, start_position[0]+61, start_position[1]+11, start_position[2]+61, 11)
mc.setBlocks(start_position[0]+50, start_position[1]+2, start_position[2]+50, start_position[0]+60, start_position[1]+10, start_position[2]+60, 20)
mc.setBlocks(start_position[0]+51, start_position[1]+3, start_position[2]+51, start_position[0]+59, start_position[1]+9, start_position[2]+59, 0)
