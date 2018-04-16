from building import print_tower, clean
from mcpi.minecraft import Minecraft
import RPi.GPIO as GPIO
mc = Minecraft.create()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)
x, y, z = mc.player.getPos()
build = True
try:
    while True:
        if not GPIO.input(12):
            GPIO.output(18,True)
            if build:                    
                a, b, c = mc.player.getPos()
                block = mc.getBlock(a, b-1, c)
                if block == 4 or block == 5:
                    clean(mc, a, b, c)
                else:
                    
                    x, y, z = mc.player.getPos()
                    print_tower(mc, x, y, z)
                build = False
        else:
            build = True
            GPIO.output(18, False)
except:
    GPIO.cleanup()
