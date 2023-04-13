#Create music player with keyboard controller.
#You have to be able to press keyboard: play, stop, next and previous as some keys. 
#Player has to react to the given command appropriately.
import pygame
pygame.init()

screen = pygame.display.set_mode((500, 800))
done = False
color = (0, 255, 0)



text = pygame.font.Font('images//text_type.ttf', 60)
button = text.render("hi i Am Nurblack", (False), (255, 255, 255))
buttons = [
        button.get_rect(topleft =(25,200)),
        button.get_rect(topleft =(25,275)),
        button.get_rect(topleft =(25,345)),
        button.get_rect(topleft =(25,415)),
        button.get_rect(topleft =(25,490)),
        button.get_rect(topleft =(25,560)),
        button.get_rect(topleft =(25,635)),
        button.get_rect(topleft =(25,700))
]
main = pygame.image.load('images//main page.JPG')

musics = [
        pygame.image.load('images//тату на твоем теле.JPG'),
        pygame.image.load('images//The Black.JPG'),
        pygame.image.load('images//Hotline bling.JPG'),
        pygame.image.load('images//Ne sebep.JPG'),
        pygame.image.load('images//reminder.JPG'),
        pygame.image.load('images//See You Again.JPG'),
        pygame.image.load('images//Sweather Weather.JPG'),
        pygame.image.load('images//Those Eyes (Speed up).JPG')
]

song = True
clock = pygame.time.Clock()
num = -1

while not done:
        
        if song:  
                screen.blit((main), (1, 1))
        else:
                screen.blit((musics[num]),  (0,0))
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                song = False
                                num += 1
                                num %= 7
                
 
        
        
        clock.tick(60)
        pygame.display.update()