import pygame as pg

class Button:
    def __init__(self, x, y, width, height, text, font, text_color, button_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.text_color = text_color
        self.button_color = button_color
        self.rect = pg.Rect(x, y, width, height)

    def draw(self, surface):
        # Draw the button rect
        pg.draw.rect(surface, self.button_color, (self.x, self.y, self.width, self.height))

        # Render the text
        text_surface = self.font.render(self.text, True, self.text_color)

        # Calculate the text rect
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + self.width // 2, self.y + self.height // 2)

        # Draw the text
        surface.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)