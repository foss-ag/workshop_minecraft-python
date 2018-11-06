import pygame
import math
from pygame.math import Vector2
import random
import time

# Initialisierung sowohl verschiedener Variablen und Attribute, als auch pygame
pygame.init()
size = (1000, 800)
screen = pygame.display.set_mode(size)
done = False
is_blue = True
x = 500
y = 400

acc = [0, 0]
shoots = []

astroid_timer = 100
astroids_faster = 0
#astroids = [[size[0], 100, 1, 0]]
astroids = []
health = 194

number_of_game_minutes = 4

clock = pygame.time.Clock()
image = pygame.image.load('src/player.png')
shoot = pygame.image.load('src/shoot.png')
astroid = pygame.image.load('src/astroid.png')
astroid1 = astroid
s_shoot_timer = time.time()
lifes = 5
astroid_speed = 7
player_speed = 3

# Funktionen des Spieles
def rotate_player():
	# hole Mausposition und berechne anhand des Winkels die entsprechende Rotation
	position = pygame.mouse.get_pos()
	angle = math.atan2(position[1] - (y + 27), position[0] - (x + 25))
	rotimage = pygame.transform.rotate(image, 270 - angle * 180 / math.pi)
	return position, rotimage, (x - rotimage.get_rect().width / 2, y - rotimage.get_rect().height / 2)

def write_time_life():
	font = pygame.font.Font(None, 24)
	survivedtext = font.render(
		str(int((number_of_game_minutes * 90000 - pygame.time.get_ticks()) / 60000)) + ":" + str(
			int((2 * 90000 - pygame.time.get_ticks()) / 1000 % 60)).zfill(
			2), True, (255, 255, 255))
	textRect = survivedtext.get_rect()
	textRect.topright = [size[0] - 5, 5]
	screen.blit(survivedtext, textRect)
	life_text = font.render(str(lifes), True, (255, 255, 255))
	life_text_rect = life_text.get_rect()
	life_text_rect.topright = [15, 6]
	screen.blit(life_text, life_text_rect)

def get_rect_astroid_player(astroid_inst, new_pos, rotimage):
	sizen = astroid.get_size()
	astroid_n = pygame.transform.scale(astroid, (sizen[0] * astroid_inst[2], sizen[1] * astroid_inst[2]))
	astroid_rect = pygame.Rect(astroid_n.get_rect())
	astroid_rect.top = astroid_inst[1]
	astroid_rect.left = astroid_inst[0]
	play_rect = pygame.Rect(rotimage.get_rect())
	play_rect.top = new_pos[1] - pygame.Rect(image.get_rect()).x
	play_rect.left = new_pos[0] - pygame.Rect(image.get_rect()).y
	return astroid_rect, play_rect

def get_rect_bullet(bullet):
	bullrect = pygame.Rect(shoot.get_rect())
	bullrect.left = bullet[1]
	bullrect.top = bullet[2]
	return bullrect

def create_astroid():
	# x pos, y pos, size scale, shooted
	astroids.append([size[0] - 5, random.randint(50, size[1] - 30), random.randint(1, 6), 0])

def player_astroid_collision_check(astroid_inst, astroid_rect, player_rect):
	check = astroid_rect.colliderect(player_rect)
	if check:
		astroids.remove(astroid_inst)
	return check

# Hauptschleife
while not done:
	screen.fill((0, 0, 0))

	# berechne neue Pfeil ausrichtung anhand der Maus
	position, rotimage, new_pos = rotate_player()

	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			e_shoot_time = time.time()
			if e_shoot_time - s_shoot_timer > 0.09:
				acc[1] += 1
				shoots.append(
					[math.atan2(position[1] - (y + 32), position[0] - (x + 26)), x + 32,
					 y + 32])
				s_shoot_timer = e_shoot_time

	# shooting
	for bullet in shoots:
		index = 0
		velx = math.cos(bullet[0]) * 10
		vely = math.sin(bullet[0]) * 10
		bullet[1] += velx
		bullet[2] += vely
		if bullet[1] < -64 or bullet[1] > size[0] + 40 or bullet[2] < -64 or bullet[2] > size[1] + 80:
			shoots.pop(index)
		index += 1
		for projectile in shoots:
			shoot1 = pygame.transform.rotate(shoot, 270 - projectile[0] * 180 / math.pi)
			screen.blit(shoot1, (projectile[1], projectile[2]))

	# schreibe die Spielzeit und die Anzahl der Leben
	write_time_life()

	# astroids
	##### Schritt 1
	######################### Dein Code kommt hier rein ###############################
	
	
	
	
	####################################################################################

	for astroid_inst in astroids:
		if astroid_inst[0] < -64:
			astroids.remove(astroid_inst)
		astroid_inst[0] -= astroid_speed
		astroid_rect, player_rect = get_rect_astroid_player(astroid_inst, new_pos, rotimage)
		##### Schritt 2
		######################### Dein Code kommt hier rein ###############################
		
		
		
		
		####################################################################################


		##### Schritt 3
		######################### Dein Code kommt hier rein ################################
		
		
		
		
		
		####################################################################################

	for astroid_inst in astroids:
		sizen = astroid.get_size()
		astroid_n = pygame.transform.scale(astroid, (sizen[0] * astroid_inst[2], sizen[1] * astroid_inst[2]))
		screen.blit(astroid_n, astroid_inst[:-2])


	###### Schritt 4
	######################### Dein Code kommt hier rein ###############################
	
	
	
	
	####################################################################################

	screen.blit(rotimage, new_pos)
	astroid_timer -= 1

	pygame.display.flip()
	clock.tick(60)
