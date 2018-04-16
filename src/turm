#oooooooooooooooo
#ovvvvvvvvvvvvvvo
#ovbbbbbbbbbbbbvo
#ovbnnnnnnnnnnbvo
#ovbnnnnnnnnnnbvo
#ovbnnnnnnnnnnbvo
#ovbnnnnnnnnnnbvo
#ovbnnnnnnnnnnbvo
#ovbnnnnmnnnnnbvo
#ovbnnnnnnnnnnbvo
#ovbnnnnnnnnnnbvo
#ovbnnnnnnnnnnbvo
#ovbnnnnnnnnnnbvo
#ovbbbbbbbbbbbbvo
#ovvvvvvvvvvvvvvo
#oooooooooooooooo


# ohne boden hoehe: 25

def print_tower(mc, x, y, z):
	# sei x, y, z der mittelpunkt des turmes
	# ecke 1
	q, w, r = x-8, y, z-8
	# ecke 2
	u, i, o = x+8, y, z+8
	#hier ist ein problem
	#fences
	mc.setBlocks(q, w, r, u, i+25, o, 85)
	mc.setBlocks(q+1, w, r+1, u-1, i, o-1, 0)

	a, b, c = q+2, w, r+2
	e,f,g = u-2, i, o-2
	#cobbles
	mc.setBlocks(a,b,c, e,f+30,g, 4)
	mc.setBlocks(a+1,b+1,c+1, e-1,f+29,g-1, 0)

	#door
	mc.setBlocks(a+5, b+1, c, a+7, f+3, g, 0) 

	#layers
	for i in range(0,26,5):
		mc.setBlocks(a+1, b + i, c-1, e-1, f + i, g+1, 4)
		mc.setBlocks(a-1, b + i, c+1, e+1, f + i, g-1, 5)
		
	mc.setBlocks(a + 1, b + 1, c + 1, a + 1, b + 30, c + 1, 65)

	#windows
	w1, w2, w3, w4 = a+5, b+1, c, g
	for i in range(5,26,5):
		mc.setBlocks(w1, w2 + i, w3, w1 + 2, w2 + i, w4, 0)
	mc.player.setPos(x, y + 1, z)
