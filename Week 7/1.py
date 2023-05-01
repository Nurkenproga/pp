#Create a simple clock application (only with minutes and seconds) which is synchronized with system clock.
# Use Mickey's right hand as minutes arrow and left - as seconds. For moving Mickey's hands you can use: pygame.transform.rotate
import pygame
import sys
import datetime

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Clock")
bg = pygame.image.load("images//mickey_mouse.png").convert_alpha()

arm1 = pygame.image.load("images//hand.png").convert_alpha()
arm2 = pygame.image.load("images//pales.png").convert_alpha()

while True:
    sec = datetime.datetime.now().second
    min = datetime.datetime.now().minute
    
    angle = (min * 6)
    angle1 = (sec * 6)
    
    screen.blit(bg, (0,0))
    rotated_image_1 = pygame.transform.rotate(arm1, angle)
    rotated_image_2 = pygame.transform.rotate(arm2, angle1)
        
    screen.blit(rotated_image_1, (350 - int(rotated_image_1.get_width() / 2),350 - int(rotated_image_1.get_width() / 2)))
    screen.blit(rotated_image_2, (350 - int(rotated_image_2.get_width() / 2),350 - int(rotated_image_2.get_width() / 2)))
        
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    
