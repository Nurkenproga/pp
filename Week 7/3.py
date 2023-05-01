####
#Draw circle - a red ball of size 50 x 50 (radius = 25) on white background.
#When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key. 
#The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored
####
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
done = False
red = (225, 0, 0)
black = (0, 0, 0)

pressed = pygame.key.get_pressed()

y = 50
x = 50
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
       
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 20
        if pressed[pygame.K_DOWN]: y += 20
        if pressed[pygame.K_LEFT]: x -= 20
        if pressed[pygame.K_RIGHT]: x += 20
        
        if y > 465:
                y = 465
                red = (0, 255, 0)
        if x > 765:
                red = (0, 255, 0)
                x = 765
        if x < 35:
                red = (0, 255, 0)
                x = 35
        if y < 35:
                red = (0, 255, 0)
                y = 35
  
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, red, (x, y), (25), (0))
        pygame.draw.line(screen, black, (1, 1), (800, 1), (20))
        pygame.draw.line(screen, black, (1, 1), (1, 500), (20))
        pygame.draw.line(screen, black, (800, 1), (800, 500), (20))
        pygame.draw.line(screen, black, (1, 500), (800, 500), (20))
        pygame.time.Clock().tick(60)
        pygame.display.flip()
        