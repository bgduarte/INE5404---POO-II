import json
from game import *

#------------------------------------------------------------------------------#

class HighscoresFile:
	_path = System().working_path + 'data/highscores.json'

	@classmethod
	def load(cls):
		try:
			with open(cls._path, 'r') as highscores:
				return json.load(highscores)
		
		except (FileNotFoundError, json.decoder.JSONDecodeError):
			return {}

	@classmethod
	def write(cls, minigame_name, score):
		data = cls.load()

		with open(cls._path, 'w+') as highscores:
			data[minigame_name] = max(data.get(minigame_name, 0), score)

			json.dump(data, highscores)

#------------------------------------------------------------------------------#

class HighscoresStageModel:
	def __init__(self, view):
		self._view   = view
		self._scores = HighscoresFile.load()
		self._view.on_highscores_changed(self._scores)

	def go_to_main_menu(self):
		System().current_stage = None

#------------------------------------------------------------------------------#

class HighscoresStageView:
	_background = Image('data/graphics/highscores.png', pivot=Point(0, 0))

	def __init__(self):
		self._highscores_texts = []

	def on_draw(self):
		self._background.draw(Point(0, 0))

		for i, text in enumerate(self._highscores_texts):
			text.draw(Point(80, 70 + i*20))

	def on_highscores_changed(self, highscores):
		self._highscores_texts.clear()

		for name, score in highscores.items():
			text = Text('data/fonts/adam_pro.otf', 14, (255, 255, 255))
			text.contents = '%s: %d\n' % (name, score)

			self._highscores_texts.append(text)

#------------------------------------------------------------------------------#

class HighscoresStageController:
	def __init__(self, model):
		self._model = model

	def on_mouse_event(self, position, button, pressed):
		if pressed and position.y < 50:
			self._model.go_to_main_menu()

#------------------------------------------------------------------------------#

class HighscoresStage(Stage):
	def __init__(self):
		self._view       = HighscoresStageView()
		model            = HighscoresStageModel(self._view)
		self._controller = HighscoresStageController(model)

	def on_draw(self, dt):
		self._view.on_draw()

	def on_mouse_event(self, position, button, pressed):
		self._controller.on_mouse_event(position, button, pressed)