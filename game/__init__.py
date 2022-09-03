import pygame
import sys
from game.config import constant
from game.player import Player
from game.ball import Ball
from game.bricks import Bricks
from random import randint

class Game:
    def __init__(self):

        pygame.init()
        #The code below creates, names and times the screen used to play the game
        self.screen = pygame.display.set_mode((constant.screen_width,constant.screen_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Breakout")
        #Below is the canvas fill color
        self.bg_color = pygame.Color("black")
        self.bg = self.create_bg()
        self.font = pygame.font.Font('assets/Kenney Rocket.ttf', 15)
        self.gameover = False
        self.music()
        self.player = Player()
        self.ball = Ball()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player , self.ball)
        self.bricks = Bricks(self.all_sprites)

        #crt
        self.crt = CRT()
    def music(self):
        #The -1 allows for the song to be looped
        self.music = pygame.mixer.Sound("assets/12 Virbank CIty.mp3")
        self.music.play(-1)

    def create_bg(self):
        bg = pygame.image.load("assets/ground.png").convert()
        return bg

    # If the player looses all their lives or scores max point this function will be called resetting the whole game
    def reset(self):
        self.gameover = False
        self.player = Player()
        self.ball = Ball()
        self.all_sprites.empty()
        self.all_sprites.add(self.player,self.ball)
        self.bricks = Bricks(self.all_sprites)
    def handle_events(self):
        # Allows control of the paddle with left and right keys
        keys = pygame.key.get_pressed()
        if self.gameover and keys[pygame.K_SPACE]:
            self.reset()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    def update(self):
        if self.player.points >= 96:
            self.gameover = True

        if self.ball.off_screen():
            self.player.lose_life()
            if self.player.lives <= 0:
                self.gameover = True
            self.ball.reset()
        self.ball.paddle_collide(self.player)
        self.bricks.check_collision(self.ball, self.player)
        self.all_sprites.update()
        pygame.display.update()
        self.clock.tick(64)


    def draw(self):
        self.screen.fill(self.bg_color)

        if self.gameover:
            text = self.font.render("Game over SPACE to restart", 1, pygame.Color("white"))
            self.screen.blit(text, (constant.screen_width/2 - 140, constant.screen_height /2))
        else:
            self.screen.blit(self.bg, (-120, -90))
            self.all_sprites.draw(self.screen)

            text = self.font.render('points: {0}'.format(self.player.points), 1, pygame.Color("white"))
            self.screen.blit(text, (120, 1))
            for i in range(self.player.lives):
                x = i * 20
                self.screen.blit(self.player.heart, (x, 4))
            #crt
            self.crt.draw()


#This class is purely cosmetic providing a retro aesthetic to the game
class CRT:
    def __init__(self):
        vignette = pygame.image.load("assets/tv.png").convert_alpha()
        self.scale = pygame.transform.scale(vignette, (constant.screen_width, constant.screen_height))
        self.screen = pygame.display.get_surface()
        self.create_tv_lines()
    def draw(self):
        self.scale.set_alpha(randint(75, 90))
        self.screen.blit(self.scale, (0, 0))

    def create_tv_lines(self):
        line_height = 4
        line_amount = constant.screen_height // line_height
        for line in range(line_amount):
            y = line * line_height
            pygame.draw.line(self.scale, 'black', (0, y), (constant.screen_width, y), 1)

