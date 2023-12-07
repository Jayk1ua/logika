from pygame import *

#створи вікно гри
window = display.set_mode((700,500))

background = transform.scale(image.load('background.png'), (700, 500))
sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
x = 0
y = 300

sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
x1 = 50
y1 = 300


clock = time.Clock()
FPS = 60

run = True

while run:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x, y))
    window.blit(sprite2, (x1, y1))
    

    for e in event.get():
        if e.type == QUIT:
            run = False


    keys_pressed = key.get_pressed()
    

    if keys_pressed[K_UP]:
        y -= 10


    if keys_pressed[K_DOWN]:
        y += 10

    if keys_pressed[K_RIGHT]:
        x += 10

    if keys_pressed[K_LEFT]:
        x -= 10



    if keys_pressed[K_w]:
        y1 -= 10

    if keys_pressed[K_s]:
        y1 += 10

    if keys_pressed[K_d]:
        x1 += 10

    if keys_pressed[K_a]:
        x1 -= 10














    display.update()
    clock.tick(FPS)
#задай фон сцени

#створи 2 спрайти та розмісти їх на сцені

#оброби подію «клік за кнопкою "Закрити вікно"»