import pygame
from mvc.start.start_view import Start_view
from state.start_state import StartState
from mvc.start.start_controller import Start_controller
from mvc.win.win_view import Win_view
from state.win_state import WinState
from mvc.win.win_controller import Win_controller
from mvc.lost.lost_view import Lost_view
from state.lost_state import LostState
from mvc.lost.lost_controller import Lost_controller
from mvc.play.play_view import Play_view
from state.play_state import PlayState
from mvc.play.play_controller import Play_controller
from mvc.play.play_model import Play_model




class Game:
    def __init__(self):
        self.win_count = 0
        self.lost_count = 0

        self.pg = pygame
        self.pg.init()
        self.pg.font.init()
        self.rect_font = self.pg.font.SysFont('Comic Sans MS', 30)
        self.window_size = 330
        self.scr = self.pg.display.set_mode((self.window_size,self.window_size))

        start_view = Start_view(self.scr, self.pg)
        self.currentState = StartState(start_view, Start_controller(start_view))

        winview = Win_view(self.scr, self.pg)
        winstate = WinState(winview, Win_controller(winview))
        self.winstate = winstate

        lostview = Lost_view(self.scr, self.pg)
        loststate = LostState(lostview, Lost_controller(lostview))
        self.loststate = loststate

    def setState(self, state):
        self.currentState = state
    
    def next_state(self):
        if isinstance(self.currentState, StartState):
            playmodel = Play_model(10)
            playview = Play_view(self.scr, self.pg, 10)
            playstate = PlayState(playmodel, playview, Play_controller(playmodel, playview))
            
            self.setState(playstate)

        elif isinstance(self.currentState, PlayState):
            if self.currentState.win:
                self.winstate.inc_count_win()
                self.setState(self.winstate)
            else:
                self.setState(self.loststate)

        elif isinstance(self.currentState, WinState) or isinstance(self.currentState, LostState):
            playmodel = Play_model(10)
            playview = Play_view(self.scr, self.pg, 10)
            playstate = PlayState(playmodel, playview, Play_controller(playmodel, playview))
            self.setState(playstate)

        
    def run(self): 
        while True:
            res = self.currentState.do()
            if res:
                break
            self.next_state()


g = Game()
g.run()