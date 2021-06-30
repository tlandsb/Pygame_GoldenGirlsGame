#import
import pygame
import random

#initializations
pygame.init()
pygame.mixer.init()

#display
backgroundImage = pygame.image.load('Level_3_Background.jpg')
display_width = backgroundImage.get_size()[0]
display_height = backgroundImage.get_size()[1]

gameDisplay = pygame.display.set_mode((display_width, display_height))

input_box = pygame.Rect(426, 170, 140, 32)

#pygame.display.set_mode((400, 300), pygame.FULLSCREEN)   /Full Screen Option/
pygame.display.set_caption('Golden Girls Game')

#colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

#pygame.display.set_mode((400, 300), pygame.FULLSCREEN)   /Full Screen Option/
pygame.display.set_caption('Thank you for being a friend')

#colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)


#fonts
all_fonts = pygame.font.get_fonts()
font = pygame.font.SysFont("comicsansms", 50)
text = font.render("Dorthy", True, blue)
fontgameover = pygame.font.SysFont("comicsansms", 20)
textgameover = fontgameover.render("START", True, green)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 60))                 #every pygame object must have
        self.image.fill(blue)
        self.rect = self.image.get_rect(center=(86, 43))     #every pygame object must have
        self.hitbox = self.rect
        self.energyMeter = 50

    def moveRight(self):
        self.rect.x += 10
    def moveLeft(self):
        self.rect.x -= 10
    def moveJump(self):
        self.rect.y -= 10
    def moveDown(self):
        self.rect.y += 10

    # def hit(self):
    #     if self.




class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(display_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.hitbox = self.rect

    def update(self):
        self.rect.x += self.speedx + 10
        self.rect.y += self.speedy + 10
        if self.rect.top > display_height + 10 or self.rect.left < -25 or self.rect.right > display_width + 20:
            self.rect.x = random.randrange(display_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)



class GoalItems(object):
    def __init__(self, x, y):
        self.image = pygame.Surface((10, 10))
        self.image.fill(green)
        self.rect = pygame.Rect(x, y, 10, 10)
        self.x = x
        self.y = y

    def draw(self, win):
        gameDisplay.blit(self.image, (self.x, self.y))

#clock
clock = pygame.time.Clock()

#sprites
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

goalItem1 = GoalItems(644, 445)
# goalItem2 = GoalItems(1103, 673)
# goalItem3 = GoalItems(1247, 114)

for i in range(20):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


# #main loop
done=False
while not done:
        event = pygame.event.get()
        keys = pygame.key.get_pressed()
        ##Player Movement
        if keys[pygame.K_RIGHT]:
            player.moveRight()
        elif keys[pygame.K_LEFT]:
            player.moveLeft()
        elif keys[pygame.K_UP]:
            player.moveJump()
        elif keys[pygame.K_DOWN]:
            player.moveDown()

        ##print(keys)
        mouse = pygame.mouse.get_pos()
        print(mouse)

        gameDisplay.blit(backgroundImage, (0, 0))
        ##all_sprites.moveRight()
        all_sprites.draw(gameDisplay)
        all_sprites.update()

        goalItem1.draw(gameDisplay)
        # goalItem2.draw(gameDisplay)
        # goalItem3.draw(gameDisplay)

        #
        # if pygame.sprite.spritecollideany(player, Mob):
        #     print("yes sprite")

        if (goalItem1.rect.colliderect(player.rect)):
            width = max(200, text.get_width() + 10)
            input_box.w = width
            # Blit the text.
            gameDisplay.blit(text, (input_box.x - 250, input_box.y))
            # Blit the input_box rect.
            pygame.draw.rect(gameDisplay, blue, input_box, 2)
            pygame.display.update()


        pygame.display.update()
