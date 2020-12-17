from game import *

#------------------------------------------------------------------------------#

class PausedStageModel:
	def __init__(self, view, paused_stage):
		self._view         = view
		self._paused_stage = paused_stage

	def unpause(self):
		System().current_stage = self._paused_stage

	def go_to_main_menu(self):
		System().current_stage = None

#------------------------------------------------------------------------------#

class PausedStageView:
	_background = Image('data/graphics/paused.png', pivot=Point(0, 0))

	def on_draw(self):
		self._background.draw(Point(0, 0))

#------------------------------------------------------------------------------#

class PausedStageController:
	def __init__(self, model):
		self._model = model

	def on_key_event(self, key, pressed):
		if pressed and key == K_ESCAPE:
			self._model.unpause()
	
	def on_mouse_event(self, position, button, pressed):
		if pressed and 132 <= position.x < 268:
			if position.y < 150:
				self._model.unpause()

			else:
				self._model.go_to_main_menu()

#------------------------------------------------------------------------------#

class PausedStage(Stage):
	def __init__(self, paused_stage):
		self._view       = PausedStageView()
		model            = PausedStageModel(self._view, paused_stage)
		self._controller = PausedStageController(model)
	
	def on_draw(self, dt):
		self._view.on_draw()

	def on_key_event(self, key, pressed):
		self._controller.on_key_event(key, pressed)
	
	def on_mouse_event(self, position, button, pressed):
		self._controller.on_mouse_event(position, button, pressed)