import pygame, random
from random import randint

WIDTH = 1200
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bloodseeker")
clock = pygame.time.Clock()

def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)


def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

class Player1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("img/player1a.png").convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 50
		self.rect.centery = HEIGHT //3
		self.speed_x = 0
		self.hp = 100
		self.mana = 100
		

	def update(self):
		
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp < 0:
			self.hp = 0
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speed_x = -7
		if keystate[pygame.K_d]:
			self.speed_x = 7
		self.rect.x += self.speed_x
		if keystate[pygame.K_w]:
			self.speed_y = -7
		if keystate[pygame.K_s]:
			self.speed_y = 7
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH + self.rect.centerx +1:
			self.rect.right = WIDTH + self.rect.centerx+ 1
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > 700:
			self.rect.bottom = 700

class Player2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("img/player2a.png").convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 50
		self.rect.centery = HEIGHT * 2//3
		self.speed_x = 0
		self.hp = 100
		self.mana = 100
		

	def update(self):
		
		
		#self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp < 0:
			self.hp = 0
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -7
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 7
		self.rect.x += self.speed_x
		if keystate[pygame.K_UP]:
			self.speed_y = -7
		if keystate[pygame.K_DOWN]:
			self.speed_y = 7
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH + self.rect.centerx + 1:
			self.rect.right = WIDTH + self.rect.centerx +1
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > 700:
			self.rect.bottom = 700

class Enemy(pygame.sprite.Sprite):
	
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/blood/blood0.png").convert(),(200,200))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH//2
		
		self.rect.centery = HEIGHT//2
		self.cast = False
		
		self.blood = False
		self.rangspell = 10
		self.rangcancel = 10
		self.counter = True
    
	def update(self):
		self.centerx = WIDTH//2
		

class Rupture(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = rupture_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50 # VELOCIDAD DE LA animación

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(rupture_anim):
				self.kill()
			else:
				center = self.rect.center
				self.image = rupture_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center

def show_go_screen():
	
	screen.fill(BLACK)#(background, [0,0])
	draw_text1(screen, "Bloodseeker", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "llega a la meta", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	#draw_text(screen, "Created by: Francisco Carvajal", 10,  60, 625)
	
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

####----------------Rupture IMAGENES --------------
rupture_anim = []
for i in range(22):
	file = "img/blood/blood{}.png".format(i)
	img = pygame.image.load(file).convert()
	img.set_colorkey(WHITE)
	img_scale = pygame.transform.scale(img, (200,200))
	rupture_anim.append(img_scale)

background = pygame.image.load("img/fond.png").convert()

rupture_sound = pygame.mixer.Sound("sound/rupture.wav")

game_over = True
running = True
while running:
	if game_over:

		show_go_screen()
		screen.blit(background,(0,0))
		game_over = False
		
		all_sprites = pygame.sprite.Group()
		
		enemy = Enemy()
		player1 = Player1()
		player2 = Player2()
		all_sprites.add(enemy ,player1, player2)
		
	
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			break


		keystate = pygame.key.get_pressed()

		if not enemy.blood:
			player1.image = pygame.image.load("img/player1a.png").convert()
			player2.image = pygame.image.load("img/player2a.png").convert()
			if enemy.counter:
				time1 = pygame.time.get_ticks()
				if (time1//100) % randint(10,30) == 0:
					print(time1//100)
					rupture = Rupture(enemy.rect.center)
					all_sprites.add(rupture)
					enemy.counter = False	
				
					time2 = pygame.time.get_ticks()
					if (time2//100) % 20 == 0:
						print(time2//100)
						enemy.cast = True
						rupture_sound.play()
		
		if enemy.cast:
			enemy.blood = True
				
		if enemy.blood:
			
			player1.image = pygame.image.load("img/player1b.png").convert()
			
			if keystate[pygame.K_a]:
				player1.hp -= 5
			if keystate[pygame.K_w]:
				player1.hp -= 5
			if keystate[pygame.K_d]:
				player1.hp -= 5
			if keystate[pygame.K_s]:
				player1.hp -= 5
		
			player2.image = pygame.image.load("img/player2b.png").convert()
			
			if keystate[pygame.K_LEFT]:
				player2.hp -= 5
			if keystate[pygame.K_DOWN]:
				player2.hp -= 5
			if keystate[pygame.K_RIGHT]:
				player2.hp -= 5
			if keystate[pygame.K_UP]:
				player2.hp -= 5
			time3 = pygame.time.get_ticks()
			if (time3//100) % randint(10,30) == 0:
				enemy.counter = True
				enemy.cast = False
				enemy.blood = False
			
		
		if player1.hp == 0:
			player1.rect.centerx = 50
			player1.rect.centery = HEIGHT //3
			player1.hp = 100
		if player2.hp == 0:
			player2.rect.centerx = 50
			player2.rect.centery = HEIGHT * 2//3
			player2.hp = 100
		if player1.rect.centerx > WIDTH:
			game_over = True
		if player2.rect.centerx > WIDTH:
			game_over = True
	all_sprites.update()

	

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	#Marcador
	
	#draw_text(screen, str(player.score), 25, WIDTH // 2, 10)
	
	# Escudo.
	draw_hp_bar(screen, 5, 5, player1.hp)
	draw_text2(screen, str(int(player1.hp)) + "/100", 10, 50, 5)
	draw_hp_bar(screen, 600, 5, player2.hp)
	draw_text2(screen, str(int(player2.hp))+ "/100", 10, 650, 5)
	draw_mana_bar(screen, 5, 15, player1.mana)
	draw_text2(screen, str(int(player1.mana))+ "/100", 10, 50, 15)
	draw_mana_bar(screen, 600, 15, player2.mana)
	draw_text2(screen, str(int(player2.mana))+ "/100", 10, 650, 15)

	pygame.display.flip()
pygame.quit()