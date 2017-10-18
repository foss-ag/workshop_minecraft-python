- from mcpi.minecraft import Minecraft
- from mcpi import block
- mc = Minecraft.create()

- 1. mc.postToChat('Hello World')
- 2. hallo = 'Hello World'
     mc.postToChat(hallo)
- 3. pos = mc.Player.getPos()
     mc.postToChat(pos)
- 4. pos = mc.Player.getPos()
     mc.setBlock(pos.X, pos.Y, pos.Z + 1, block.STONE)
- 5. while True:
	mc.postToChat(mc.Player.getPos())

-----Blumen-Aufgabe-----

- 1. indizes = [1,2,3,4,5,6,7,8,9,10]
     pos = mc.Player.getPos()
     for index in indizes:
	mc.setBlock(pos.X, pos.Y, pos.Z + index, block.STONE)
- 2. waehle_block = True
	while True:
		hits = mc.events.pollBlockHits()
		for hit in hits:
			if waehle_block:
				mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.WATER)
				waehle_block = False
			else:
				mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.LAVA)
				waehle_block = True
-------shuffle--------

- 1. mc.postToChat(random.randint(1,5))

