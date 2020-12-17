from game import *

#------------------------------------------------------------------------------#

class GameOverStage(Stage):
	_background = Image('data/graphics/game_over.png', pivot=Point(0, 0))

	def __init__(self, score):
		self._transition_timer = Timer(4, self._go_to_main_menu)
		self._score            = Text('data/fonts/adam_pro.otf', 16)
		self._score.contents   = str(score)

	def on_draw(self, dt):
		self._background.draw(Point(0, 0))
		self._score.draw(Point(204, 176))

	def on_update(self, dt):
		self._transition_timer.advance(dt) 

	def _go_to_main_menu(self):
		System().current_stage = None