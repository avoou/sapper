

class PlayState:
    def __init__(self,  model, view, controller) -> None:
        self.model = model
        self.view = view
        self.controller = controller
        self.win = None

    def do(self):
        self.view.main_view()
        res = self.controller.main_run()
        self.win = self.controller.win
        return res