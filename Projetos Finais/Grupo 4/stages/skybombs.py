import random, math
from game import *
from pygame.locals import *
from pygame.mixer import Sound
from stages.gameover import GameOverStage
from stages.paused import PausedStage
from stages.highscores import HighscoresFile
from hud import HealthScoreHUD

#------------------------------------------------------------------------------#

class Bomb(GameObject):
	_image = Image('data/graphics/bomb.png')
	_sound = Sound('data/sounds/bomb.wav')

	def __init__(self):
		super().__init__()

		self._velocity     = 100
		self._acceleration = 150

	@property
	def dimensions(self):
		return self._image.dimensions

	def on_draw(self):
		self._image.draw(self.position)

	def on_explode(self, reached_ground=False):
		self._sound.play()
		System().current_stage.despawn_bomb(self)

		if reached_ground:
			System().current_stage.decrease_life()
	
	def on_update(self, dt):
		self._velocity  += self._acceleration * dt
		self.position.y += self._velocity * dt

#------------------------------------------------------------------------------#

class AvoidBomb(Bomb):
	_image = Image('data/graphics/avoid_bomb.png')

	def on_explode(self, reached_ground=False):
		super().on_explode(not reached_ground)

#------------------------------------------------------------------------------#

class ClearBomb(Bomb):
	_image = Image('data/graphics/clear_bomb.png')

	def on_explode(self, reached_ground=False):
		super().on_explode(reached_ground)

		if not reached_ground:
			for bomb in System().current_stage.list_active_bombs():
				if not isinstance(bomb, AvoidBomb):
					bomb.on_explode()

#------------------------------------------------------------------------------#

class Cannon(GameObject):
	HIT_RADIUS = 12
	ANIMATION_FADEOUT_TIME = 0.1

	_image = Image('data/graphics/cannon.png', pivot=Point(7, 9))
	_beam  = Image('data/graphics/cannon_beam.png', pivot=Point(0, 4))
	_sound = Sound('data/sounds/cannon.wav')

	def __init__(self):
		width, height = System().get_screen_size()

		super().__init__(Point(width/2, height - self._image.height))

		self._draw_beam                = False
		self._shooting_animation_timer = Timer(self.ANIMATION_FADEOUT_TIME,
															self._hide_beam)

	def fire_at(self, position):
		self._draw_beam = True
		self._shooting_animation_timer.reset()
		self._sound.play()

		for bomb in System().current_stage.list_active_bombs():
			distance = bomb.position.distance_to_line(position, self.position)

			if distance <= self.HIT_RADIUS:
				bomb.on_explode()

	def on_draw(self):
		if self._draw_beam:
			self._beam.draw(self.position, self.rotation)

		self._image.draw(self.position, self.rotation)

	def on_update(self, dt):
		self._shooting_animation_timer.advance(dt)

		self.rotation = -(System().get_mouse_position() - self.position).angle()

	def _hide_beam(self):
		self._draw_beam = False

#------------------------------------------------------------------------------#

class SkyBombsStage(Stage):
	BOMB_TYPES = (Bomb, AvoidBomb, ClearBomb)
	SPAWN_RATE_INCREASE = 0.05
	
	_preview    = Image('data/graphics/sky_bombs_preview.png', pivot=Point(0, 0))
	_background = Image('data/graphics/sky_bombs_background.png', 
							  pivot=Point(0, 0))

	def __init__(self):
		self._bombs       = []
		self._spawn_timer = Timer(2, self.spawn_bomb_randomly, repeat=True)
		self._cannon      = Cannon()
		self._hud         = HealthScoreHUD(text_color=(0, 0, 0))
		self._lives       = 5
		self._score       = 0

	def decrease_life(self):
		self._lives -= 1

	def despawn_bomb(self, bomb):
		if bomb in self._bombs:
			self._bombs.remove(bomb)
			self._score += 1

	def list_active_bombs(self):
		return self._bombs.copy()

	@classmethod
	def get_preview(cls):
		return cls._preview

	def on_draw(self, dt):
		self._background.draw(Point(0, 0))

		for bomb in self._bombs:
			bomb.on_draw()

		self._cannon.on_draw()
		self._hud.draw(lives=self._lives, score=self._score)

	def on_key_event(self, key, pressed):
		if pressed and key == K_ESCAPE:
			System().current_stage = PausedStage(self)

	def on_mouse_event(self, position, button, pressed):
		if pressed and button == BUTTON_LEFT:
			self._cannon.fire_at(position)
 
	def on_update(self, dt):
		self._spawn_timer.advance(dt)
		self._spawn_timer.fuse *= 1 - self.SPAWN_RATE_INCREASE * dt

		for bomb in self._bombs:
			bomb.on_update(dt)

		self._explode_bombs_on_ground()
		self._cannon.on_update(dt)

		if self._lives <= 0:
			HighscoresFile.write('Sky Bombs', self._score)
			System().current_stage = GameOverStage(self._score)

	def spawn_bomb_randomly(self):
		width, height = System().get_screen_size()

		bomb = random.choice(self.BOMB_TYPES)()

		bomb_width, bomb_height = bomb.dimensions

		bomb.position.x = random.randint(bomb_width/2, width - bomb_width/2)
		bomb.position.y = -bomb_height/2

		self._bombs.append(bomb)

	def _explode_bombs_on_ground(self):
		_, height  = System().get_screen_size()
		to_explode = []

		for bomb in self._bombs:
			_, bomb_height = bomb.dimensions

			if bomb.position.y >= height - bomb_height:
				to_explode.append(bomb)
			
		for bomb in to_explode:
			bomb.on_explode(reached_ground=True)