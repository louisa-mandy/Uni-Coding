import pygame 

class Ship():

  def __init__(self, ai_settings, screen):
    # creating the ship and setting it to its starting point
    self.screen = screen
    self.ai_settings = ai_settings 

    # load the ship image 
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    
    # for the ship to start at the very bottom of the screen
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

    #storing a decimal value for the ships center 
    self.center = float(self.rect.centerx)
    
    #set the movement left/right
    self.moving_right = False
    self.moving_right = False 
    
  def update(Self):
    #updating the ships position
    if self.moving_right and self.rect.right < self.screen_rect.right:
        self.center += self.ai_settings.ship_speed_factor
    if self.moving_left and self.rect.left > 0:
        self.center -= self.ai_settings.ship_speed_factor

    # Update rect object from self.center.
    self.rect.centerx = self.center

    def blitme(self):
    #Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
