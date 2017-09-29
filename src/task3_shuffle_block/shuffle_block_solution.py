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


while True:
	#check if a block is hit and get the coordinates
	for hit in mc.events.pollBlockHits():
		#get the block
		block = mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)
		#if the hit block is in the list take the next block
		if block in block_list:
			i = (block_list.index(block)+1)%10
		else:
			#start with index 0
			i = 0
		#change the block
		mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block_list[i])

###############easy version#######################
i = 0
while True:
	# check if a block is hit and get the coordinates
	for hit in mc.events.pollBlockHits():
		#set the block with the current index
		mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block_list[i])
	#if the index is 9 then the next index should be 0
	if i == 9:
		i = 0
	#else increment the index
	else:
		i += 1
