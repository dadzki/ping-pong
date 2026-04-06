from pygame import *

w = 700
h = 500
window = display.set_mode((w, h))
display.set_caption('ping-pong')
background = transform.scale(image.load('background.jpg'), (w, h))
clock = time.Clock()
FPS = 60
game = True
finish = False
font.init()
font1 = font.SysFont('Calibry', 70)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.height = player_height
        self.width = player_width
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < h - self.height:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < h - self.height:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__(player_image, player_x, player_y, player_width, player_height, player_speed)
        self.speed_x = player_speed
        self.speed_y = player_speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if sprite.collide_rect(self, platform1):
            self.speed_x = self.speed
        if sprite.collide_rect(self, platform2):
            self.speed_x = -self.speed
        if self.rect.y < 0 or self.rect.y > h - self.height:
            self.speed_y *= -1


platform1 = Player('platform.png', 50, 200, 16, 100, 3)
platform2 = Player('platform.png', 650, 200, 16, 100, 3)
ball = Ball('ball.png', 350, 250, 32, 32, 3)


while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        

    
    platform1.reset()
    platform2.reset()
    ball.reset()
    if not finish:
        platform1.update()
        platform2.update2()
        ball.update()
    else:
        window.blit(end_text, (100, 200))
    if ball.rect.x > w:
        end_text = font1.render('Победил игрок слева', True, (255, 190, 0))
        finish = True
    if ball.rect.x < 0:
        end_text = font1.render('Победил игрок справа', True, (255, 190, 0))
        finish = True
    display.update()
    clock.tick(FPS)


