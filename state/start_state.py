

class StartState:
    def __init__(self, view, controller) -> None:
        self.view = view
        self.controller = controller

    def do(self):
        self.view.main_view()
        res = self.controller.main_run()
        return res