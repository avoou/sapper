from random import randint

class Start_view:
    def __init__(self, scr, pygame):
        self.pg = pygame
        self.scr = scr
        self.rect_font = self.pg.font.SysFont(name='',size=30) #'Comic Sans MS',
        self.window_size = self.scr.get_size()[0]

    def main_view(self):
        textwin = "PLAY"
        random_color = (randint(90,100), randint(80,90), randint(95,102))
        width_textwin, height_textwin = self.pg.font.Font.size(self.rect_font, textwin)
        x = (self.window_size/2) - width_textwin/2
        y = (self.window_size/2) - height_textwin/2
        self.pg.Surface.fill(self.pg.display.get_surface(), color=random_color)
        textsurface = self.rect_font.render(textwin, False, (130, 200, 30))
        self.start_button = self.pg.draw.rect(self.scr, random_color, self.pg.Rect(x, y, width_textwin, height_textwin))
        self.scr.blit(textsurface,(x,y))
        self.pg.display.flip()