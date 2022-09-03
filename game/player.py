import pygame
from game.config import constant

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/paddleBlu.png").convert_alpha()
        self.rect = self.image.get_rect()
        #Sets up the paddle sprite in the middle of the screen
        self.y_pos = constant.screen_height - 50
        self.x_pos = constant.screen_width // 2
        self.rect.center = (self.x_pos, self.y_pos)
        #This is required to increase and decrease the velocity of the ball based on the direction of the paddle is moving
        self.direction = 0
        self.lives = constant.init_lives
        self.points = constant.init_points
        self.heart = pygame.image.load("assets/heart.png").convert_alpha()

    def update(self):
        #This is to make sure that the paddle sprite is locked onto the screen
        if self.x_pos < 52:
           self.x_pos = 52
        if self.x_pos > constant.screen_width - 52:
           self.x_pos = constant.screen_width - 52
        self.rect.center = (self.x_pos, self.y_pos)




    def lose_life(self):
       self.loose_life_sound()
       self.lives -= 1
        #This function is called everytime the player looses a life
    def loose_life_sound(self):
        self.lfsound = pygame.mixer.Sound("assets/sounds_fail.wav")
        self.lfsound.play()
        #This is called when a brick is destroyed
    def gain_point(self):
        self.points += 1

    def gameover(self):
        #This is initially set to 5 lives
        self.lives = constant.init_lives

    def move_right(self):
        #Called from handle events when right arrow button is pressed
        self.x_pos += constant.x_vel
        self.direction = +1

    def move_left(self):
        # Called from handle events when left arrow button is pressed
        self.x_pos -= constant.x_vel
        self.direction = -1