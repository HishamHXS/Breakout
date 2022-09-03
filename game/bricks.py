import pygame
from game.config import constant
# This consists all the sprites for the blocks
bricks = [
"assets/element_blue_rectangle.png",
"assets/element_green_rectangle.png",
"assets/element_red_rectangle.png",
"assets/element_green_rectangle.png",
"assets/element_yellow_rectangle.png",
"assets/element_purple_rectangle.png",
"assets/element_yellow_rectangle.png",
"assets/element_red_rectangle.png",
"assets/element_yellow_rectangle.png",
"assets/element_purple_rectangle.png",
"assets/element_yellow_rectangle.png",
"assets/element_red_rectangle.png",
]

class Bricks:
      def __init__(self, all_sprites):
          self.all_sprites = all_sprites
          self.all_bricks = pygame.sprite.Group()
          #initiliasing all of the bricks
          for r in range(constant.brick_rows):
              for c in range(constant.brick_col):
                  brick = Brick(r, c)
                  self.all_sprites.add(brick)
                  self.all_bricks.add(brick)
      def check_collision(self, ball, player):
          collision_list = pygame.sprite.spritecollide(ball, self.all_bricks, False)
          for brick in collision_list:
              ball.bounce()
              player.gain_point()
              self.brick_sound()
              brick.kill()
      #called everytime a brick is contacted by the ball
      def brick_sound(self):
          self.brsound = pygame.mixer.Sound("assets/sounds_impact.wav")
          self.brsound.play()


#Brick inherits from sprite
#This class is responsible for drawying the brick sprites
class Brick(pygame.sprite.Sprite):
      def __init__(self, row, col):
          super().__init__()
          self.x_pos = constant.brick_start + (col*64) + 32
          self.y_pos = constant.brick_start + (row*32) + 16
          self.image = pygame.image.load(bricks[row])
          self.rect = self.image.get_rect()
          self.rect.center = (self.x_pos, self.y_pos)



