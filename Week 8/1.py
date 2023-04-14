####
#Draw circle - a red ball of size 50 x 50 (radius = 25) on white background.
#When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key. 
#The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored
####
import pygame
import random

pygame.init()
# стэйтментс
screen = pygame.display.set_mode((840, 650))
done = False
red = (225, 0, 0)
black = (0, 0, 0)
enemy = pygame.image.load("images//enemy_car.png").convert_alpha()
car = pygame.image.load("images//main_car-removebg-preview.png").convert_alpha()
track = pygame.image.load("images//track.png").convert_alpha()
pressed = pygame.key.get_pressed()
tenge = pygame.image.load("images//tenge.png").convert_alpha()
bg = 0
text = pygame.font.Font('images//text_type.ttf', 80)
enemy_x = 585
enemy_y = -200
car_y = 450 
car_x = 500
tenge_timer = pygame.USEREVENT + 1
tenge_list = []
x = 0
game = True
lose = text.render("Game over", False, (0, 0, 0))
score = text.render("Score   ", False , (193, 196, 192))

#Таймер монетки
pygame.time.set_timer(tenge_timer, 2500)
while not done:
        if game:
            # передвижение монеты
            tenge_x = random.randrange(175, 685)
            tenge_y = random.randrange(0,100)
            
            # квадратики что бы взаимодействовать
            coin = text.render(str(x), False, (144,238, 144))
            car_rect = car.get_rect(topleft=(car_x, car_y))
            enemy_rect = enemy.get_rect(topleft=(enemy_x, enemy_y))
            
            #проиграть
            if car_rect.colliderect(enemy_rect):
                print("gg")
                game = False
            bg += 5

            #рисуем наши рисунки
            if bg == 650:  bg = 0
            screen.blit(track, (0, bg - 650))
            screen.blit(track,(0, bg))
            screen.blit(enemy, (enemy_x,enemy_y))
            screen.blit(car, (car_x, car_y))
            screen.blit(score, (545,0))
            screen.blit(coin, (755, 0))
            enemy_y = enemy_y + 15

            #монетка убираеться появляеться 
            if tenge_list:
                for (i, element) in enumerate(tenge_list):
                    screen.blit(tenge, element)
                    element.y += 5
                    if element.y >= 650:
                        tenge_list.pop(i)
                # если машина собереть монетку
                if car_rect.colliderect(element):
                    print(x) 
                    x= x + 1
                    tenge_list.pop(i)
            
            #передвижение машинок
            if enemy_y > 800:
                enemy_y = -200
                enemy_x =random.randrange(125, 585)
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: car_y -= 20
            if pressed[pygame.K_DOWN]: car_y += 20
            if pressed[pygame.K_LEFT]: car_x -= 20
            if pressed[pygame.K_RIGHT]: car_x += 20
        
            if car_y > 520: car_y = 520
            if car_x > 585: car_x = 585
            if car_x < 125: car_x = 125
            if car_y < 300: car_y = 300
        #экран проирыша   
        else:
            screen.fill((87,88,89))
            screen.blit(lose, (200,200))
        #монетка в листе появлялось     
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == tenge_timer:
                    tenge_list.append(tenge.get_rect(topleft= (tenge_x, tenge_y)))
            
        #фпс и дисплэй флип
        pygame.time.Clock().tick(60)
        pygame.display.update()
        