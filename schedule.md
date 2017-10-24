- Einführung in Python + Blumen-Aufgabe
    - Erklärung
        - Code werden in .py Dateien geschrieben und ausgeführt über das Terminal mit dem Befehl python DATEINAME
    - Imports
            from mcpi.minecraft import Minecraft
            from mcpi import block
            mc = Minecraft.create()
    - Chat
            mc.postToChat('Hello World')
    - Variablen
            text = 'Hello World'
            mc.postToChat(text)
    - Positionen
            pos = mc.Player.getPos()
            mc.postToChat(pos)
    - Blöcke setzen
            pos = mc.Player.getPos()
            mc.setBlock(pos.X, pos.Y, pos.Z + 1, block.STONE)
    - while-Schleifen
            while True:
                mc.postToChat(mc.Player.getPos())

- Shuffle Block
    - for-Schleifen
            indices = [1,2,3,4,5,6,7,8,9,10]
            pos = mc.Player.getPos()
            for index in indizes:
	           mc.setBlock(pos.X, pos.Y, pos.Z + index, block.STONE)
            Zugriff mit Index zeigen
    - Bedingungen
            toggle = True
            while True:
		          hits = mc.events.pollBlockHits()
                  for hit in hits:
                  if toggle:
                    mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.WATER)
                    toggle = False
                  else:
                    mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.LAVA)
                	toggle = True

- Lava Runner
    - Zufallszahlen
            mc.postToChat(random.randint(1,5))
