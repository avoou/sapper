

class Lost_controller:
    def __init__(self, view):
        self.view = view

    def main_run(self):
        done = False
        while not done:
            for event in self.view.pg.event.get():
                if event.type == self.view.pg.QUIT:  
                    done = True
                    return True
                if event.type == self.view.pg.MOUSEBUTTONDOWN and event.button == 1:
                    if self.view.restart_button.collidepoint(event.pos):
                        done = True
                        return False
