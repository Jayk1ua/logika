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


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        


class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= win_width - 80:
            self.direction = 'left'
        

class Wall(sprite.Sprite):
    def __init__(self, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.width = wall_width
        self.height = wall_height
        
        self.image = Surface((self.width, self.height))
        self.image.fill((137, 226, 70))


        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))













#Вікно

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money_sound = mixer.Sound('money.ogg')
kick_sound = mixer.Sound('kick.ogg')

font.init()
f = font.Font(None, 70)

win = f.render("YOU WIN", True, (137, 255, 70))
lose = f.render("YOU LOSE", True, (255, 0, 0))


#Картинки
background = scale(load('background.jpg'), (win_width, win_height))


w1 = Wall(15, 0, 20, 400)
w2 = Wall(15, 0, 160, 20)
w3 = Wall(170, 0, 20, 130)
w4 = Wall(170, 110, 90, 20)
player =Player('hero.png', 5, win_height - 80, 4, )
monster = Enemy('cyborg.png', win_width - 150, win_height - 220, 2 )
treasure = GameSprite('treasure.png', win_width - 80, win_height - 80, 0)


clock = time.Clock()
FPS = 60

walls = [w1, w2, w3, w4]




run = True
finish = False

#Ігровий цикл
while run:
    
    



    for e in event.get():
        if e.type == QUIT:
            run = False



    if not finish:
        window.blit(background,(0, 0))
        player.reset()
        monster.reset()
        treasure.reset()


        for wall in walls:
            wall.reset()

        if sprite.collide_rect(player, treasure):
            finish = True
            window.blit(win,(200, 200))
            money_sound.play()
        
        if sprite.collide_rect(player, monster):
            finish = True
            window.blit(lose,(200, 200))
            kick_sound.play()

        for wall in walls:
            if sprite.collide_rect(player, wall):
                finish = True
                window.blit(lose, (200, 200))
                kick_sound.play()











    player.update()
    monster.update()
    display.update()
    clock.tick(FPS)