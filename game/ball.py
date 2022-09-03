import pygame
from game.config import constant
from random import randint

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = constant.screen_width //2
        self.y_pos = constant.screen_height //2
        # convert alpha allows for us to remove the excess black pixels on sprites to be removed
        self.image = pygame.image.load("assets/ballBlue.png").convert_alpha()
        self.rect = self.image.get_rect()
        # The ball starts with a random velocity making the game harder and more enjoyable
        self.vel = [randint(1, 5), randint(-4, 4)]
        self.rect.center = (self.x_pos, self.y_pos)

    def update(self):
        #This code allows for the ball to rebounded if it hits either of the side walls through changing the direction of the velocity (velocity has both magnitude and direction)
        #The 11 represents the size of the ball sprite
        if self.x_pos < 11 or self.x_pos > constant.screen_width - 11:
            self.vel[0] = -self.vel[0]
        if self.y_pos < 11:
            self.vel[1] = -self.vel[1]
        if self.vel[0] == 0:
            self.vel[0] += 1
        if self.vel[1] == 0:
            self.vel[1] += 1
        self.x_pos += self.vel[0]
        self.y_pos += self.vel[1]

        self.rect.center = (self.x_pos, self.y_pos)
    def reset(self):
        #If the ball goes out of bound we want to return it back to the center of frame
        self.vel = [randint(2, 4), randint(-4, 4)]
        self.x_pos = constant.screen_width // 2
        self.y_pos = constant.screen_height // 2
        self.rect.center = (self.x_pos, self.y_pos)

    def paddle_collide(self, paddle):
        if self.rect.colliderect(paddle.rect):
            if abs(self.rect.bottom - paddle.rect.top) < constant.collision_thresh and self.vel[1] > 0:
               self.vel[1] = -self.vel[1]
               #This allows for the user to change the velocity of the ball
               self.vel[0] += paddle.direction
               if self.vel[0] > constant.max_ball_vel:
                  self.vel[0] = constant.max_ball_vel
               if self.vel[0] < -constant.max_ball_vel:
                  self.vel[0] = -constant.max_ball_vel
            else:
                self.vel[0] += -1

    #This checks if the ball goes past the bottom of the screen
    def off_screen(self):
        return self.y_pos > constant.screen_height
    #First index represents x direction while second represent y direction
    #Python index starts at 0
    def bounce(self):
        self.vel[0] = -self.vel[0]
        self.vel[1] = randint(-2, 2)