from game import *

#------------------------------------------------------------------------------#

class HealthScoreHUD:
	_heart = Image('data/graphics/heart.png', pivot=Point(0, 0))

	def __init__(self, text_color):
		self._score = Text('data/fonts/adam_pro.otf', 14, text_color)
	
	def draw(self, lives=0, score=0):
		width, _ = System().get_screen_size()

		self._score.contents = str(score)
		self._score.draw(Point(4, 12))

		for i in range(lives):
			self._heart.draw(Point(width - (13 + i * (self._heart.width + 2)), 2))