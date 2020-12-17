from game import *
from pygame.locals import *
from stages.skybombs import SkyBombsStage
from stages.wildwest import WildWestStage
from stages.highscores import HighscoresStage

#------------------------------------------------------------------------------#

class MainMenuStageModel:
	_MINIGAMES = (SkyBombsStage, WildWestStage)

	def __init__(self, view):
		self._view           = view
		self._selected_index = 0
		self._view.on_minigame_changed(self._selected_minigame)

	def go_to_next_minigame(self):
		self._selected_index = (self._selected_index + 1) % len(self._MINIGAMES)
		self._view.on_minigame_changed(self._selected_minigame)

	def go_to_previous_minigame(self):
		self._selected_index = (self._selected_index - 1) % len(self._MINIGAMES)
		self._view.on_minigame_changed(self._selected_minigame)

	def start_selected_minigame(self):
		System().current_stage = self._selected_minigame()

	def enter_highscores(self):
		System().current_stage = HighscoresStage()

	@property
	def _selected_minigame(self):
		return self._MINIGAMES[self._selected_index]

#------------------------------------------------------------------------------#

class MainMenuStageView:
	_background = Image('data/graphics/main_menu.png', pivot=Point(0, 0))

	def __init__(self):
		self._minigame_preview = None

	def on_draw(self):
		self._background.draw(Point(0, 0))
		self._minigame_preview.draw(Point(150, 153))

	def on_minigame_changed(self, value):
		self._minigame_preview = value.get_preview()

#------------------------------------------------------------------------------#

class MainMenuStageController:
	def __init__(self, model):
		self._model = model

	def on_key_event(self, key, pressed):
		if pressed:
			if key == K_LEFT:
				self._model.go_to_previous_minigame()
			
			elif key == K_RETURN:
				self._model.start_selected_minigame()
			
			elif key == K_RIGHT:
				self._model.go_to_next_minigame()

	def on_mouse_event(self, position, button, pressed):
		if pressed:
			if 153 <= position.y < 228:
				if position.x < 150:
					self._model.go_to_previous_minigame()

				elif position.x < 250:
					self._model.start_selected_minigame()
			
				else:
					self._model.go_to_next_minigame()
				
			elif position.x >= 350 and position.y >= 260:
				self._model.enter_highscores()

#------------------------------------------------------------------------------#

class MainMenuStage(Stage):
	def __init__(self):
		self._view       = MainMenuStageView()
		model            = MainMenuStageModel(self._view)
		self._controller = MainMenuStageController(model)

	def on_draw(self, dt):
		self._view.on_draw()

	def on_key_event(self, key, pressed):
		self._controller.on_key_event(key, pressed)

	def on_mouse_event(self, position, button, pressed):
		self._controller.on_mouse_event(position, button, pressed)