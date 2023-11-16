#створи гру "Лабіринт"!
from pygame import *
from pygame.transform import scale, flip
from pygame.image import load
from random import randint




#GameSprite
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = scale(load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#Вікно

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

#Картинки
background = scale(load('background.jpg'), (win_width, win_height))


player = GameSprite('hero.png', 5, win_height - 80, 4, )
monster = GameSprite('cyborg.png', win_width - 150, win_height - 220, 2 )



clock = time.Clock()
FPS = 60






run = True


#Ігровий цикл
while run:
    window.blit(background, (0, 0))
    player.reset()
    monster.reset()


    for e in event.get():
        if e.type == QUIT:
            run = False















    
    display.update()
    clock.tick(FPS)