#Створи власний Шутер!
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint


#window
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))

background = scale(load('galaxy.jpg'), (win_width, win_height))
clock = time.Clock()
FPS = 60

#music
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
mixer.music.set_volume(0.2)




#GameSprite
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed


    def fire(self):
        pass


#об'єкти
rocket = Player('rocket.png', 5, win_height - 100, 90, 100, 4)
#asteroid = ('asteroid.png', )



#Ігровий цикл
run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False



    if not finish:
        window.blit(background,(0, 0))
        rocket.reset()
        rocket.update()























    display.update()
    clock.tick(FPS)