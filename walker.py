import pygame as pg

import random

class Walker:
    def __init__(self, rect, dimensions, lifespan):
        self.rect = rect
        self.x = rect.x
        self.y = rect.y
        self.w, self.h = dimensions
        self.lifespan = lifespan
        self.current_lifespan = 0
        self.black = pg.Color(0,0,0,255)
        self.ocean_color = pg.Color(5, 65, 219)
        self.sand_color = pg.Color(192, 176, 32)
        self.grassland_color = pg.Color(1, 69, 0)
        self.highland_color = pg.Color(25, 51, 0)
        self.mountain_color = pg.Color(51, 51, 0)
        self.highpeak_color = pg.Color(82, 78, 72)
        self.is_alive = True
        
    def move(self):
        if self.current_lifespan >= self.lifespan:
            self.is_alive = False
        
        d = random.randint(1,4)
        
        if d == 1 and self.y <= self.h - 10:     # DOWN
            self.y += 4
        if d == 2 and self.y > 10:   # UP
            self.y -= 4
        if d == 3 and self.x <= self.w - 10:   # RIGHT
            self.x += 4
        if d == 4 and self.x > 10:   # LEFT
            self.x -= 4
            
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.current_lifespan += 1
        
    
    def change_color(self, screen):
        bg_color = screen.get_at((self.x, self.y))
        if bg_color == self.ocean_color:
            return self.sand_color 
        if bg_color == self.sand_color:
            return self.grassland_color
        if bg_color == self.grassland_color:
            return self.highland_color
        if bg_color == self.highland_color:
            return self.mountain_color
        if bg_color == self.mountain_color:
            return self.highpeak_color
        return self.grassland_color
        