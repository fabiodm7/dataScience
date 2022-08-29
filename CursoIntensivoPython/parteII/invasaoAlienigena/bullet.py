import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,
            ai_settings.bullet_width,ai_settings.bullet_height
        )
        self.rect_lateral_right = pygame.Rect(0,0,
            ai_settings.bullet_height,ai_settings.bullet_width
        )
        self.rect_lateral_left = self.rect_lateral_right.copy()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        
        self.rect_lateral_right.centery = ship.rect.centery
        self.rect_lateral_left.centery = ship.rect.centery
        
        self.rect_lateral_right.right = ship.rect.right
        self.right = float(self.rect.right)

        self.rect_lateral_left.left = ship.rect.left
        self.left = float(self.rect.left)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

        self.right += self.speed_factor
        self.rect_lateral_right.right = self.right

        self.left -= self.speed_factor
        self.rect_lateral_left.left = self.left

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        pygame.draw.rect(self.screen,self.color,self.rect_lateral_right)
        pygame.draw.rect(self.screen,self.color,self.rect_lateral_left)