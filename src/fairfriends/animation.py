import mcpi.minecraft as minecraft
import mcpi.block as block
from gpiozero import LED
import time

mc = minecraft.Minecraft.create()

# get player position and clean area
(x, y, z) = mc.player.getPos()
mc.setBlock(x, y, z+1, x+51, y+27, z+6, block.AIR)

# define all necessary position for the writings
# each triple includes a position (x and y) and the used color
F1 = [(x, 23) for x in range(5, 9)] + [(5, y) for y in range(16, 24)] + [(6, 20), (7, 20)]
a1 = [(x, y) for x in [10, 13] for y in range(16, 21)] + [(x, y) for x in [11, 12] for y in [16, 20]]\
     + [(14, 18), (15, 17), (16, 16)]
i1 = [(18, y) for y in range(16, 21)] + [(18, 22)]
r1 = [(20, y) for y in range(16, 21)] + [(21, 19), (22, 20)]
F2 = [(x+13, y-11) for (x, y) in F1]
r2 = [(x+3, y-11) for (x, y) in r1]
i2 = [(x+8, y-11) for (x, y) in i1]
e  = [(28, y) for y in range(5, 10)] + [(29, y) for y in [5, 7, 9]] + [(30, y) for y in [5, 7, 8, 9]]
n  = [(32, y) for y in range(5, 10)] + [(36, y) for y in range(5, 9)] + [(33, 8), (34, 9), (35, 9)]
d  = [(38, y) for y in range(5, 10)] + [(41, y) for y in range(5, 13)]\
     + [(x, y) for x in [39, 40] for y in [5, 9]]
s1 = [(43, y) for y in [5, 7, 8, 9]] + [(44, y) for y in [5, 7, 9]] + [(45, y) for y in [5, 6, 7, 9]]

fairfriends = F1+a1+i1+r1+F2+r2+i2+e+n+d+s1

F3 = [(x+5, y-6) for (x, y) in F1]
o  = [(15, y) for y in range(10, 15)] + [(18, y) for y in range(10, 15)] + [(x, y) for x in [16, 17] for y in [10, 14]]
s2 = [(x-23, y+5) for (x, y) in s1]
s3 = [(x+4, y) for (x, y) in s2]
h  = [(x, 12) for x in range(28, 31)]
A  = [(x, y) for x in [32, 35] for y in range(10, 18)] + [(x, y) for x in [33, 34] for y in [14, 17]]
G  = [(37, y) for y in range(10, 18)] + [(38, 10), (38, 17)] + [(x, y) for x in [39, 40] for y in [10, 13, 17]]\
     + [(41, y) for y in [10, 11, 12, 13, 17]]

foss_ag = F3+o+s2+s3+h+A+G

leds_g_r = ["g": LED(2),"r": LED(3)]

def get_color(pos):
    if pos in F1:
        return 1
    elif pos in a1:
        return 2
    elif pos in i1:
        return 3
    elif pos in r1:
        return 4
    elif pos in F2:
        return 5
    elif pos in r2:
        return 6
    elif pos in i2:
        return 9
    elif pos in e:
        return 10
    elif pos in n:
        return 11
    elif pos in d:
        return 13
    elif pos in s1:
        return 14
    else:
        return 0

build_fairfriends = True
positions = [(x, y) for x in range(51) for y in range(27)]
while True:
    leds_g_r["g"].off()
    leds_g_r["r"].on()
    for (xp, yp) in positions:
        if build_fairfriends:
            mc.setBlock(x+xp, y+yp, z+3, 35, get_color((xp, yp)))
        else:
            if (xp, yp) in foss_ag:
                mc.setBlock(x+xp, y+yp, z+3, 35, 13)
            else:
                mc.setBlock(x+xp, y+yp, z+3, 35, 0)
    build_fairfriends = not build_fairfriends
    leds_g_r["r"].off()
    leds_g_r["g"].on()
    # TODO fit duration
    time.sleep(5)

    for (xp, yp) in positions:
        mc.setBlock(x, y, z + 3, 0)
