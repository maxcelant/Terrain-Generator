import pygame as pg
import sys

from walker import Walker
from button import Button

pg.init()

def init():
    size = (w, h) = (1080, 720)
    screen = pg.display.set_mode(size)
    screen.fill(pg.Color(5, 65, 219))
    pg.display.set_caption('Terrain Generator')
    return screen, (w, h)

def create_button(pos, w, text):
    x, y = pos
    return Button(x=x, 
                  y=y, 
                  width=w, height=30,
                  text=text,
                  font = pg.font.Font(None, 24),
                  text_color=pg.Color(255,255,255),
                  button_color=pg.Color(0, 0, 0))

def create_walker(pos, w, h, lifespan):
    rect_dimensions = (4, 4)
    rect = pg.Rect(pos, rect_dimensions)
    return Walker(rect=rect, dimensions=(w, h), lifespan=lifespan)

def main():
    
    screen, (w, h) = init()
    clock = pg.time.Clock()

    font = pg.font.Font(None, 24)
    text_surface = font.render("[P] to pause, [R] to reset", True, (255, 255, 255))
    screen.blit(text_surface, (5, h - 20))
    
    walkers = []      # Holds all the walkers created
    is_running = True # Pause/Unpause mechanic
    lifespan = 500    # Starting lifespan 
    
    # Buttons for increasing and decreasing the walker lifespan
    inc_button = create_button((20, 20), 150, "Increase Lifespan")
    dec_button = create_button((180, 20), 160, "Decrease Lifespan")
    inc_button.draw(screen)
    dec_button.draw(screen)
    
    lifespan_surface = pg.Surface((200, 20))
    
    mouse_button_down = False
    
    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                key = event.key
                if key == pg.K_p:
                    is_running = not is_running
                if key == pg.K_r:
                    screen.fill(pg.Color(5, 65, 219))
                    screen.blit(text_surface, (5, h - 20))
                    inc_button.draw(screen)
                    dec_button.draw(screen)
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_button_down = True
                if event.button == 1:
                    if inc_button.is_clicked(event.pos):
                        lifespan += 500
                        break
                    if dec_button.is_clicked(event.pos):
                        lifespan -= 200
                        break
                    else:
                        walkers.append(create_walker(event.pos, w, h, lifespan))
            if event.type == pg.MOUSEBUTTONUP:
                mouse_button_down = False
            if event.type == pg.MOUSEMOTION:
                if mouse_button_down:
                    walkers.append(create_walker(event.pos, w, h, lifespan))
        
        lifespan_text = font.render(f'Lifespan: {lifespan}', True, (255, 255, 255))
        lifespan_surface.fill(pg.Color(5, 65, 219))
        lifespan_surface.blit(lifespan_text, (0, 0))
        screen.blit(lifespan_surface, (w - 140, 30))
        
        if is_running:
            
            for walker in walkers:
                if walker.is_alive: 
                    walker.move()
                    pg.draw.rect(surface=screen, 
                            color=walker.change_color(screen), 
                            rect=walker.rect)
            
        pg.display.update()
        clock.tick(1000)
    
    
if __name__ == '__main__':
    main()