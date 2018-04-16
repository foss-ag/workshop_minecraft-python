def build_staircase(mc, x, y, z, h):
    stats = [1, 3, 0, 2]
    mc.setBlocks(x, y, z, x-2, y+h, z-2, 0)
    cx, cz = -1, 0
    j = 1
    xzb = True
    xzv = -1
    stat = 0
    mc.setBlock(x, y, z, 67, stats[stat])
    y = y+1
    for i in range(0, h-1):
        mc.setBlock(x + cx, y + i, z + cz, 67, stats[stat])
        if j % 2 == 0:
            xzb = not xzb
            if j % 4 == 0:
                xzv *= -1
            if j % 8 == 0:
                stat = 0
            else:
                stat += 1
        j += 1
        cx = (cx+xzv) if xzb else cx
        cz = (cz+xzv) if not xzb else cz
        
    if cx - cz % 2 == 0:
        mc.setBlock(x + cx, y + h - 2, z + cz, 4)

def clean(mc, x, y, z):
    mc.setBlocks(x-9, y-1, z-9, x+9, y+30, z+9, 0)
    
def print_tower(mc, x, y, z):
    # sei x, y, z der mittelpunkt des turmes
    # ecke 1
    height = 30
    q, w, r = x-8, y, z-8
    # ecke 2
    u, i, o = x+8, y, z+8
    mc.setBlocks(q-1, w-1, r-1, u+1, i-1, o+1, 2)
    #hier ist ein problem
    mc.setBlocks(q-1, w, r-1, u+1, i+height + 10, o+1, 0)
    #fences
    mc.setBlocks(q-1, w, r-1, u+1, w, o+1, 85)
    mc.setBlocks(q, w, r, u, w, o, 0)

    a, b, c = q+2, w, r+2
    e,f,g = u-2, i, o-2
    #cobbles
    mc.setBlocks(a,b,c, e,f+height,g, 4)
    mc.setBlocks(a+1,b+1,c+1, e-1,f+height-1,g-1, 0)

    #door
    mc.setBlocks(a+5, b+1, c, a+7, f+3, g, 0) 

    #layers
    for i in range(0,26,5):
            mc.setBlocks(a-1, b + i, c-1, e+1, f + i, g+1, 4)
            mc.setBlocks(a+2, b + i, c+2, e-2, f + i, g-2, 5)

    #mc.setBlocks(a + 1, b + 1, c + 1, a + 1, b + 30, c + 1, 65)
    #mc.setBlocks(a + 1, b + 1, g - 1, a + 1, b + 30, g - 1, 65)
    #mc.setBlocks(e - 1, b + 1, c + 1, e - 1, b + 30, c + 1, 65)
    #mc.setBlocks(e - 1, b + 1, g - 1, e - 1, b + 30, g - 1, 65)
    build_staircase(mc, a+3, b+1, c+3, height)
    #windows
    w1, w2, w3, w4 = a+5, b+1, c, g
    q1, q2, q3, q4 = a, b+1, c+5, e
    for i in range(5,26,5):
            mc.setBlocks(w1, w2 + i, w3, w1 + 2, w2 + i + 1, w4, 0)
            mc.setBlocks(q1, q2 + i, q3, q4, q2 + i + 1, q3+2, 0)
    mc.player.setPos(x, y + 1, z)


