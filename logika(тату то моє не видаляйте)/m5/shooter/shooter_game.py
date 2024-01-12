#Створи власний Шутер!
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint
lost = 0
score = 0

#window
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))

background = scale(load('galaxy.jpg'), (win_width, win_height))
clock = time.Clock()
FPS = 60

#sound
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
mixer.music.set_volume(0.1)

fire_sound = mixer.Sound('fire.ogg')
fire_sound.set_volume(0.1)


#GameSprite + класи
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
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 25, 35, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y>win_height:
            self.rect.y=0
            self.rect.x=randint(0, win_width-80)
            lost = lost + 1
            print(lost)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

#об'єкти
rocket = Player('rocket.png', 5, win_height - 100, 90, 100, 4)

bullets = sprite.Group()


monsters = sprite.Group()
for i in range(5):
    mon = Enemy('ufo.png', randint(0, win_width-80), 0, 80, 50, randint(1, 5))
    monsters.add(mon)

#Текст
font.init()
font1 = font.SysFont('Arial', 36)

font2 = font.SysFont('Arial', 80)
txt_lose_game = font2.render('ТИ ПРОГРАВ:(', True, (220, 0, 0))
txt_win_game = font2.render('ТИ ВИГРАВ:)', True, (0, 225, 0))

font3 = font.SysFont('Arial', 50)
txt_timer = font3.render('Гра почнеться через 5 секунд', True, (255, 255, 0))

font4 = font.SysFont('Arial', 60)
txt_skipped = font4.render('Пропустив 40 астероідів', True, (220, 0, 0))

#Ігровий цикл
run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocket.fire()
                fire_sound.play()
                


    #If not finish
    if not finish:
        window.blit(background,(0, 0))

        rocket.reset()
        rocket.update()

        txt_lose = font1.render(f'Пропущено: {lost}', True, (255,0,0))
        window.blit(txt_lose, (10, 50))

        txt_win = font1.render(f'Рахунок: {score}', True, (0,255,0))
        window.blit(txt_win, (10, 20))

        

        monsters.draw(window)
        monsters.update()
        
        bullets.draw(window)
        bullets.update()

        if sprite.spritecollide(rocket, monsters, False):
            finish = True
            window.blit(txt_lose_game, (120, 180))


        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            mon = Enemy('ufo.png', randint(0, win_width-80), 0, 80, 50, randint(1, 5))
            monsters.add(mon)
            score = score + 1

        
        if score == 20:
            finish = True
            window.blit(txt_win_game, (130, 180))
        
        if lost == 40:
            finish = True
            
            window.blit(txt_skipped, (75, 180))
            txt_lost = font1.render(f'Пропущено: {lost}', True, (255,0,0))
            window.blit(txt_lose, (10, 50))

    else:
        finish = False
        score = 0
        lost = 0

        for b in bullets:
            b.kill()


        for m in monsters:
            m.kill()




        window.blit(txt_timer, (75, 260))
        display.update()
        time.delay(5000)

        for i in range(5):
            mon = Enemy('ufo.png', randint(0, win_width-80), 0, 80, 50, randint(1, 5))
            monsters.add(mon)






















    display.update()
    clock.tick(FPS)
