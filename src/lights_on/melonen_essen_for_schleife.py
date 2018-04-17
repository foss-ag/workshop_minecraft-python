from mcpi.minecraft import Minecraft
from time import sleep, time
from random import randint
from threading import Thread

TIEFE = 15

def init(mc, x, y, z, weite):
	# initialisiert die Arena
	radius = 0
	if weite % 2 == 1:
		radius = weite / 2
	else:
		radius = (weite + 1) / 2
	mc.setBlocks(x - radius, y + TIEFE, z - radius, x + radius, y - TIEFE, z + radius, 0)
	mc.setBlocks(x - radius, y - TIEFE, z - radius, x + radius, y - TIEFE, z + radius, 10)
	mc.setBlocks(x - radius, y - 1, z - radius, x + radius, y - 1, z + radius, 89, 1)
	mc.setBlocks(x - radius, y-1, z - radius, x - radius - 1, y - 1, z - radius - 1, 49)


def place_tap_stones(mc, x, y, z, weite, anzahl):
	# setzt zufaellig Melonen auf das Spielfeld
        radius = 0
        if weite % 2 == 1:
                radius = weite / 2
        else:
                radius = (weite + 1) / 2
	count = 0
	x_pre, z_pre = 0, 0
	x = int(x)
	z = int(z)
	while count < anzahl:
		pos_x = randint(x - radius + 1, x - 1)
		pos_z = randint(z - radius + 1, z - 1)
		if abs(pos_x - x_pre) < 2 or abs(pos_z - z_pre) < 2:
			continue
		x_pre, z_pre = pos_x, pos_z
		mc.setBlock(pos_x, y, pos_z, 103)
		count += 1

def check_tapped(mc, anzahl, x_timeout):
	# methode fuer den thread, die darauf achtet, ob Melonen geschlagen wurden und diese entfernt
	count = 0
	x_old = time()
	x_cur = time()
	while True:
		############################## Deinen Code hier ###############################
		
		
		
		################################################################################
		# wenn x_timeout Zeit keine Melone geschlagen wurde, dann brich ab
		x_cur = time()
		if x_cur - x_old > x_timeout:
			mc.postToChat("Du musst die Melonen schneller kriegen")
			return
		if anzahl == count:
			mc.postToChat("Du hast gewonnen!")
			return

def run_game():
	# haupt funktion
	mc = Minecraft.create()
	x_s, y_s, z_s = mc.player.getPos()
	# Variablen fuer die weite der arena, die anzahl der Melonen, Zeit
	weite = 20
	anzahl = 5
	init(mc, x_s, y_s, z_s, weite)
	game_start = False
	x_start = 0
	x_cur = 0
	x_end = 120
	# initialisiere thread
	thr = Thread(target=check_tapped, args=(mc, anzahl, 5))
	radius = 0
        if weite % 2 == 1:
                radius = weite / 2
        else:
                radius = (weite + 1) / 2
        count = 0
	while True:
		if not game_start:
			# warte bis Spieler das Obsidian betreten hat und starte das spiel
			x, y, z = mc.player.getPos()
			block_unter = mc.getBlock(x, y - 1, z)
			if block_unter == 49:
				game_start = True
				# setze die Melonen, starte die Zeit und den Thread
				place_tap_stones(mc, x_s, y_s, z_s, weite, anzahl)
				thr.start()
				x_start = time()
		else:
			# so lange, wie der Thread lebt, fuehre auch das Spiel aus
			if thr.isAlive():
				x_cur = time()
				if x_cur - x_start > x_end:
					# ist die Zeit abgelaufen, ziehe dem Spieler den Boden unter den Fuessen weg und beende das Spiel
					mc.setBlocks(x_s - radius, y_s - 1, z_s - radius, x_s + radius, y_s - 1, z_s + radius, 0)
					mc.postToChat("Du hast verloren!")
					break
				# wenn der Block im Spieler Lava ist, beende das Spiel
				# postToChat evtl entfernen, Spam auf Chat
				# mc.postToChat("Noch %i Sekunden"%(int(x_end - x_cur + x_start)))
				x, y, z = mc.player.getPos()
				block = mc.getBlock(x, y, z)
				if block == 10 or block == 11:
					mc.postToChat("Du hast verloren")
					break
				block = mc.getBlock(x, y - 1, z)
				sleep(0.1)
				# wenn Spieler auf glowstone steht, dann entferne dieses nach 0.1 Sekunde
				if block == 89:
					mc.setBlock(x, y-1, z, 0)
			else:
				break


if __name__ == "__main__":
	# starte alles	
	run_game()
