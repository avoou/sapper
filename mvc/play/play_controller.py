import pygame

class Play_controller:
    def __init__(self, model, view):
        self.right_mouse_button = 3
        self.left_mouse_button = 1
        self.model = model
        self.view = view
        self.win_set = set()
        self.count_of_flags = len(self.model.list_of_bombs)
        self.real_count_of_flags = 0
        self.win = None

    def handler_lmb(self, mouse_position):
        mod_req = None
        for key in self.view.id_rect_hash_table.keys():
            if self.view.id_rect_hash_table[key].collidepoint(mouse_position):
                mod_req = self.model.calc_field(key)
                break
        self.view.paint_open_sq(mod_req)

    def handler_rmb(self, mouse_position):
        for key in self.view.id_rect_hash_table.keys():
            if self.view.id_rect_hash_table[key].collidepoint(mouse_position):
                mf = self.model.make_flag(key)
                if mf:
                    self.view.unpaint_flag(key)
                    break
                #если клетка не закрашена. можно закрасить только определенное количество клеточек
                elif mf is not None:
                    self.view.paint_flag(key)
                    break
                else:
                    break

    def main_run(self):
        done = False  
        while not done:
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    done = True
                    return True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if event.button == self.left_mouse_button:
                        try:
                            self.handler_lmb(mouse_pos)
                        except:
                            self.win = self.model.win
                            done = True
                            return False
                            
                    elif event.button == self.right_mouse_button:
                        try:
                            self.handler_rmb(mouse_pos)
                        except:
                            self.win = self.model.win
                            done = True
                            return False