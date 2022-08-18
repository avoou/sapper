from random import randint


class Play_view:
    def __init__(self, scr, pygame, size_of_field):
        self.field = None
        self.id_rect_hash_table = {}
        self.size_of_field = size_of_field
        self.pg = pygame
        self.rect_font = self.pg.font.SysFont(name='',size=30)#'Comic Sans MS', 30
        self.scr = scr
        self.color = (10,180,41) 
        self.x = 10
        self.y = 10

    def main_view(self):
        color=(randint(90,100), randint(80,90), randint(95,102))
        self.pg.Surface.fill(self.pg.display.get_surface(), color=color)
        num_id = 0
        for num in range(self.size_of_field):
            for _ in range(self.size_of_field):
                rect_obj = self.pg.draw.rect(self.scr, (49,80,randint(75,82)), self.pg.Rect(self.x, self.y, 30, 30))
                self.id_rect_hash_table[num_id] = rect_obj
                num_id += 1
                self.x += 30 + 1
            self.y += 30 + 1
            self.x = 10
            self.pg.display.flip()

    def unpaint_flag(self, key):
        push_obj = self.id_rect_hash_table[key]                                 
        self.pg.draw.rect(self.scr, (49,80,randint(75,82)), self.pg.Rect(push_obj.x, push_obj.y, 30, 30))
        self.pg.display.flip()

    def paint_flag(self, key):
        push_obj = self.id_rect_hash_table[key]                                                 
        self.pg.draw.rect(self.scr, (149,80,50), self.pg.Rect(push_obj.x, push_obj.y, 30, 30))
        self.pg.display.flip()
    
    def paint_open_sq(self, mod_req):
        if mod_req is not None:
            for id in mod_req:
                self.pg.draw.rect(self.scr, (49,80,randint(95,102)), self.pg.Rect(self.id_rect_hash_table[id].x, self.id_rect_hash_table[id].y, 30, 30))
                textsurface = self.rect_font.render(str(mod_req[id]), False, (50, 50, 50))
                self.scr.blit(textsurface,(self.id_rect_hash_table[id].x+int(30/4), self.id_rect_hash_table[id].y+int(30/4)))
                self.pg.display.flip()