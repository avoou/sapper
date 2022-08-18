

class WinState:
    def __init__(self, view, controller):
        self.view = view
        self.controller = controller

    def inc_count_win(self):
        self.controller.inc_count_win()

    def do(self):
        self.view.main_view()
        res = self.controller.main_run()
        return res