#Create music player with keyboard controller.
#You have to be able to press keyboard: play, stop, next and previous as some keys. 
#Player has to react to the given command appropriately.
import pygame
pygame.init()

screen = pygame.display.set_mode((414, 800))
done = False
color = (0, 255, 0)
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

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
songs = [
        pygame.mixer.Sound("Music//Tatu_on_your_body.mp3"), 
        pygame.mixer.Sound("Music//ASKING-ALEXANDRIA-The-Black-Official-Music-Video.mp3"),
        pygame.mixer.Sound("Music//Drake-Hotline-Bling-Official-Audio.mp3"), 
        pygame.mixer.Sound("Music//Ne_sebep.mp3"),
        pygame.mixer.Sound("Music//The-Weeknd-Reminder-Audio.mp3"), 
        pygame.mixer.Sound("Music//See-You-Again-Clean-Tyler-The-Creator-Kali-Uchis.mp3"),
        pygame.mixer.Sound("Music//The-Neighbourhood-Sweater-Weather-Lyrics.mp3"),
        pygame.mixer.Sound("Music//New-West-Those-Eyes-Lyrics-sped-up-cause-all-of-the-small-th.mp3")
]

text = pygame.font.Font('images//text_type.ttf', 80)
player = False
song = True
clock = pygame.time.Clock()
num = -1
music = -1
mouse = pygame.mouse.get_pos()
while not done:
       
        if song:  
                screen.blit((main), (1, 1))
        else:
                screen.blit((musics[num]),  (0,0))
                
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                                song = False
                                songs[music].stop()
                                num += 1
                                num %= 8
                                music += 1
                                music %= 8
                                
                        if event.key == pygame.K_LEFT:
                                song = False
                                songs[music].stop()
                                num -= 1
                                num %= 8
                                music -= 1
                                music %= 8
                        if event.key == pygame.K_SPACE:
                                if player:
                                        songs[music].stop()
                                        player = False
                                else:
                                        songs[music].play()
                                        player = True

                        
        
        
        clock.tick(60)
        pygame.display.update()