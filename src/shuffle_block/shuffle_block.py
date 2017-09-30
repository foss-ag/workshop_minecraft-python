import mcpi.minecraft as minecraft
import mcpi.block as blocks

mc = minecraft.Minecraft.create()

#List of blocks that has to be iterated
block_list = [
 blocks.STONE,
 blocks.WOOD_PLANKS,
 blocks.LAPIS_LAZULI_BLOCK,
 blocks.IRON_BLOCK,
 blocks.TNT,
 blocks.MOSS_STONE,
 blocks.DIAMOND_BLOCK,
 blocks.OBSIDIAN,
 blocks.ICE,
 blocks.MELON
 ]

block_list = [cur_block.id for cur_block in block_list]

######################################################


#your code here


######################################################
