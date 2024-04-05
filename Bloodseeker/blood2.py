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
		self.rect.centery = HEIGHT //5
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
			self.speed_x = -4
		if keystate[pygame.K_d]:
			self.speed_x = 4
		self.rect.x += self.speed_x
		if keystate[pygame.K_w]:
			self.speed_y = -4
		if keystate[pygame.K_s]:
			self.speed_y = 4
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
		self.rect.centery = HEIGHT //4
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
			self.speed_x = -4
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 4
		self.rect.x += self.speed_x
		if keystate[pygame.K_UP]:
			self.speed_y = -4
		if keystate[pygame.K_DOWN]:
			self.speed_y = 4
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH + self.rect.centerx + 1:
			self.rect.right = WIDTH + self.rect.centerx +1
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > 700:
			self.rect.bottom = 700

class Borde(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/borde.png").convert(),(1000,1))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 350

class Finish(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/finish.png").convert(),(100,350))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 350

class Enemy(pygame.sprite.Sprite):
	
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/blood/blood0.png").convert(),(200,200))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH//2
		self.rect.centery = HEIGHT//2
		self.blood = False
		self.rangcancel = 10
		self.counter = True
		self.counter2 = True
		self.a = randint(1000,5000)
		self.b = randint(1000,5000)
    
	def update(self):
		pass
		

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
		if self.frame == 1:
			rupture_sound.play()
		if self.frame == 15:
			enemy.blood = True

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

def show_game_over_screenp1():
	screen.fill(BLACK)
	draw_text1(screen, "Player 1 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

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

def show_game_over_screenp2():
	screen.fill(BLACK)
	draw_text1(screen, "Player 2 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

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

start = True
running = True
game_over1 = False
game_over2 = False
while running:
	if start:
		show_go_screen()
		screen.blit(background,(0,0))
		start = False
		
		all_sprites = pygame.sprite.Group()
		
		enemy = Enemy()
		player1 = Player1()
		player2 = Player2()
		borde = Borde()
		finish = Finish()
		all_sprites.add(enemy ,player1, player2, borde, finish)
		start_time1 = pygame.time.get_ticks()
		start_time2 = pygame.time.get_ticks()

	if game_over1:
		show_game_over_screenp1()
		screen.blit(background,(0,0))
		game_over1 = False
		
		all_sprites = pygame.sprite.Group()
		
		enemy = Enemy()
		player1 = Player1()
		player2 = Player2()
		borde = Borde()
		finish = Finish()
		all_sprites.add(enemy ,player1, player2, borde, finish)
		start_time1 = pygame.time.get_ticks()
		start_time2 = pygame.time.get_ticks()

	if game_over2:
		show_game_over_screenp2()
		screen.blit(background,(0,0))
		game_over2 = False
		
		all_sprites = pygame.sprite.Group()
		
		enemy = Enemy()
		player1 = Player1()
		player2 = Player2()
		borde = Borde()
		finish = Finish()
		all_sprites.add(enemy ,player1, player2, borde, finish)	
		start_time1 = pygame.time.get_ticks()
		start_time2 = pygame.time.get_ticks()
	
	clock.tick(60)
	
	if enemy.counter:
		enemy.a = randint(1000,6000)
		enemy.b = randint(1000,6000)
		enemy.counter = False
		enemy.counter2 = True

	if enemy.counter2:
		if not enemy.blood:
			current_time = pygame.time.get_ticks()
			elapsed_time = current_time - start_time1
			if elapsed_time >= enemy.a:
				rupture = Rupture(enemy.rect.center)
				all_sprites.add(rupture)
				enemy.counter2 = False
				start_time1 = current_time
						
	if enemy.blood:
		current_time2 = pygame.time.get_ticks()
		elapsed_time2 = current_time2 - start_time2
		player1.image = pygame.image.load("img/player1b.png").convert()
		player2.image = pygame.image.load("img/player2b.png").convert()
		
		if elapsed_time2 >= enemy.b:
			player1.image = pygame.image.load("img/player1a.png").convert()
			player2.image = pygame.image.load("img/player2a.png").convert()
			
			enemy.counter = True
			enemy.blood = False
			start_time2 = current_time2
			
		
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			player1.hp -= 2
		if keystate[pygame.K_w]:
			player1.hp -= 2
		if keystate[pygame.K_d]:
			player1.hp -= 2
		if keystate[pygame.K_s]:
			player1.hp -= 2
	
		if keystate[pygame.K_LEFT]:
			player2.hp -= 2
		if keystate[pygame.K_DOWN]:
			player2.hp -= 2
		if keystate[pygame.K_RIGHT]:
			player2.hp -= 2
		if keystate[pygame.K_UP]:
			player2.hp -= 2
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()
			break	
		
		if player1.hp == 0:
			player1.rect.centerx = 50
			player1.rect.centery = HEIGHT //5
			player1.hp = 100
		if player2.hp == 0:
			player2.rect.centerx = 50
			player2.rect.centery = HEIGHT //4
			player2.hp = 100
		if player1.rect.centerx > WIDTH:
			game_over = True
		if player2.rect.centerx > WIDTH:
			game_over = True

	# Checar colisiones - jugador1 - borde
	if pygame.sprite.collide_rect(player1, borde):
		if player1.speed_y > 0:
			player1.rect.bottom = borde.rect.top
		if player1.speed_y < 0:
			player1.rect.top = borde.rect.bottom
			
	# Checar colisiones - jugador2 - borde
	if pygame.sprite.collide_rect(player2, borde):
		if player2.speed_y > 0:
			player2.rect.bottom = borde.rect.top
		if player2.speed_y < 0:
			player2.rect.top = borde.rect.bottom

	# Checar colisiones - jugador1 - finish
	if pygame.sprite.collide_rect(player1, finish):
		game_over1 = True
		
	# Checar colisiones - jugador2 - finish
	if pygame.sprite.collide_rect(player2, finish):
		game_over2 = True

	all_sprites.update()

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)
	
	# Escudo.
	draw_hp_bar(screen, 5, 5, player1.hp)
	draw_text2(screen, str(int(player1.hp)) + "/100", 10, 50, 5)
	draw_hp_bar(screen, player1.rect.x, player1.rect.y, player1.hp)
	draw_hp_bar(screen, 600, 5, player2.hp)
	draw_text2(screen, str(int(player2.hp))+ "/100", 10, 650, 5)
	draw_hp_bar(screen, player2.rect.x, player2.rect.y, player2.hp)
	draw_mana_bar(screen, 5, 15, player1.mana)
	draw_text2(screen, str(int(player1.mana))+ "/100", 10, 50, 15)
	draw_mana_bar(screen, 600, 15, player2.mana)
	draw_text2(screen, str(int(player2.mana))+ "/100", 10, 650, 15)

	pygame.display.flip()
pygame.quit()