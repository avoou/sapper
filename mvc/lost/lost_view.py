from random import randint

class Lost_view:
    def __init__(self, scr, pygame):
        self.pg = pygame
        self.scr = scr
        self.rect_font = self.pg.font.SysFont('Comic Sans MS', 30)
        self.window_size = self.scr.get_size()[0]

    def main_view(self):
        color = (randint(90,100), randint(80,90), randint(95,102))
        self.pg.Surface.fill(self.pg.display.get_surface(), color=color)
        margin = 6

        text_lost = "YOU'VE LOST"
        width_text_lost, height_text_lost = self.pg.font.Font.size(self.rect_font, text_lost)
        x_lost_text = (self.window_size/2) - width_text_lost/2
        y_lost_text = (self.window_size/2) - (margin/2) - height_text_lost
        text = self.rect_font.render(text_lost, False, (50, 50, 50))
        self.scr.blit(text,(x_lost_text, y_lost_text))

        text_restart = "RESTART"
        width_text_restart, height_text_restart = self.pg.font.Font.size(self.rect_font, text_restart)
        x_restart_text = (self.window_size/2) - width_text_restart/2
        y_restart_text = (self.window_size/2) + (margin/2)
        self.restart_button = self.pg.draw.rect(self.scr, color, self.pg.Rect(x_restart_text, y_restart_text, width_text_restart, height_text_restart))
        
        textsurface = self.rect_font.render(text_restart, False, (30, 30, 30))
        self.scr.blit(textsurface,(x_restart_text, y_restart_text))
        self.pg.display.flip()