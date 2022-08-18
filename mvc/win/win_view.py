from random import randint

class Win_view:
    def __init__(self, scr, pygame):
        self.pg = pygame
        self.scr = scr
        self.rect_font = self.pg.font.SysFont('Comic Sans MS', 30)
        self.count_win = 0
        self.window_size = self.scr.get_size()[0]

    def main_view(self):
        win_surface = self.pg.display.get_surface()
        color = (randint(90,100), randint(80,90), randint(95,102))
        self.pg.Surface.fill(win_surface, color=color)
        margin = 6

        text_restart = "RESTART"
        width_text_restart, height_text_restart = self.pg.font.Font.size(self.rect_font, text_restart)
        x_restart_text = (self.window_size/2) - width_text_restart/2
        y_restart_text = (self.window_size/2) - height_text_restart/2
        self.restart_button = self.pg.draw.rect(self.scr, color, self.pg.Rect(x_restart_text, y_restart_text, width_text_restart, height_text_restart))
        textsurface = self.rect_font.render(text_restart, False, (30, 30, 30))
        self.scr.blit(textsurface,((x_restart_text, y_restart_text)))

        text_you_win = "YOU WIN"
        width_text_win, height_text_win = self.pg.font.Font.size(self.rect_font, text_you_win)
        x_restart_text = (self.window_size/2) - width_text_win/2
        y_restart_text = (self.window_size/2) - height_text_win - margin - height_text_restart/2
        text = self.rect_font.render(text_you_win, False, (50, 50, 50))
        self.scr.blit(text,(x_restart_text, y_restart_text))

        score = "YOUR SCORE: " + str(self.count_win)
        width_text_score, _ = self.pg.font.Font.size(self.rect_font, score)
        x_score_text = (self.window_size/2) - width_text_score/2
        y_score_text = (self.window_size/2) + margin + height_text_restart/2
        textscore = self.rect_font.render(score, False, (50, 50, 50))
        self.scr.blit(textscore,(x_score_text, y_score_text))

        self.pg.display.flip()