import pygame
from sys import exit
import time

pygame.init()


screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("BASKET BALL GAME")

font=pygame.font.Font("freesansbold.ttf",35)

hitsound="netswish.mp3"
misssound=("whistle.mp3")
throwsound="throw.wav"



court = pygame.transform.scale(pygame.image.load("court.jpg"),(900,600))

ball = pygame.transform.scale(pygame.image.load("basketball.png"),(80,80))
ball_rect=ball.get_rect()

ballx=0
bally=510
dirct="right"

shot=False

score=0
miss=0
shots=0

timelimit=180
start_time = time.time()

def game_over(score,miss,shots):
	screen2 = pygame.display.set_mode((900,600))
	pygame.display.set_caption("GAME OVER")
	

	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				exit()

		screen2.fill((0,100,255))
		screen2.blit(font.render("GAME OVER",True,"WHITE"),(340,0))
		
		screen2.blit(font.render("SCORE:"+str(score),True,"black"),(360,150))
		screen2.blit(font.render("MISSED:"+str(miss),True,"black"),(360,300))
		screen2.blit(font.render("SHOTS:"+str(shots),True,"black"),(360,450))
		pygame.display.update()


while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				pygame.mixer.music.load(throwsound)
				pygame.mixer.music.play()
				dirct=None
				if shot==False:shots+=1
                                                                    
				shot=True
	screen.fill("white")
	block=pygame.draw.rect(screen,"red",[410,80,80,50])
	
	elapsed_time = int(time.time()-start_time)
	if elapsed_time>timelimit:
		game_over(score,miss,shots)
		
		



	ball_rect.x = ballx
	ball_rect.y = bally
	
	screen.blit(court,(0,0))
	screen.blit(ball,(ball_rect.x,ball_rect.y))
	
	screen.blit(font.render("SCORE:"+str(score),True,"black"),(710,0))
	screen.blit(font.render("MISSED:"+str(miss),True,"black"),(0,0))
	screen.blit(font.render("SHOTS:"+str(shots),True,"black"),(360,0))
	screen.blit(font.render("TIME LEFT:"+str(timelimit-elapsed_time)+"sec",True,"black"),(580,480))
	if ballx<=0 :
		dirct="right"
	elif ballx>=820:
		dirct="left"

	if dirct=="right":
		ballx+=15
	elif dirct=="left":
		ballx-=15


	if shot==True and bally>0:
		bally-=8
		ball=pygame.transform.rotate(ball,180)



	if bally<=0:
		pygame.mixer.music.load(misssound)
		pygame.mixer.music.play()
		miss+=1
		bally=510
		dirct="right"
		ballx=0
		shot=False


	collide = pygame.Rect.colliderect(ball_rect, block)


	if collide:
		pygame.mixer.music.load(hitsound)
		pygame.mixer.music.play()
		score+=1
		bally=510
		dirct="right"
		ballx=0
		shot=False
	
	
	pygame.time.Clock().tick(80)
	pygame.display.update()
