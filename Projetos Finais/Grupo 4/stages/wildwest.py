import random
from game import *
from pygame.locals import *
from pygame.mixer import Sound
from stages.gameover import GameOverStage
from stages.paused import PausedStage
from stages.highscores import HighscoresFile
from hud import HealthScoreHUD

#------------------------------------------------------------------------------#

class Bandit:
	_image       = Image('data/graphics/bandit.png', pivot=Point(0, 29))
	_shoot_sound = Sound('data/sounds/gun.wav')
	_hurt_sound  = Sound('data/sounds/hurt.wav')

	def __init__(self):
		self._shoot_timer = Timer(1, self._shoot, repeat=True)

	def draw(self, position):
		self._image.draw(position)
	
	def is_inside_hitbox(self, position, point):
		return position.x <= point.x < position.x + self._image.width \
		and    position.y > point.y >= position.y - self._image.height

	def on_being_shot(self):
		self._hurt_sound.play()
		System().current_stage.despawn_bandit(self)

	def on_update(self, dt):
		self._shoot_timer.advance(dt)
	
	def _shoot(self):
		self._shoot_sound.play()
		System().current_stage.decrease_life()

#------------------------------------------------------------------------------#

class BulletproofBandit(Bandit):
	_image = Image('data/graphics/bulletproof_bandit.png', pivot=Point(0, 29))

	def __init__(self):
		super().__init__()
		self._health = 2

	def on_being_shot(self):
		self._hurt_sound.play()
		self._health -= 1

		if self._health <= 0:
			System().current_stage.despawn_bandit(self)

#------------------------------------------------------------------------------#

class WildWestStage(Stage):
	BANDIT_TYPES        = (Bandit, BulletproofBandit)
	SPAWN_RATE_INCREASE = 0.05
	SPAWNABLE_POSITIONS = (Point(68, 148), Point(182, 148), Point(301, 148),
								  Point(68, 254), Point(182, 254), Point(301, 254))

	_aim         = Image('data/graphics/aim.png', pivot=Point(4, 4))
	_preview     = Image('data/graphics/wild_west_preview.png', pivot=Point(0, 0))
	_shoot_sound = Sound('data/sounds/gun.wav')
	_background  = Image('data/graphics/wild_west_background.png', 
							   pivot=Point(0, 0))

	def __init__(self):
		self._bandits     = [None] * len(self.SPAWNABLE_POSITIONS)
		self._spawn_timer = Timer(2, self.spawn_bandit_randomly, repeat=True)
		self._hud         = HealthScoreHUD(text_color=(255, 255, 255))
		self._lives       = 5
		self._score       = 0

		System().set_mouse_visibility(False)

	def decrease_life(self):
		self._lives -= 1

	def despawn_bandit(self, bandit):
		if bandit in self._bandits:
			self._bandits[self._bandits.index(bandit)] = None
			self._score += 1

	@classmethod
	def get_preview(cls):
		return cls._preview

	def on_draw(self, dt):
		self._background.draw(Point(0, 0))

		for i, bandit in enumerate(self._bandits):
			if bandit is not None:
				bandit.draw(self.SPAWNABLE_POSITIONS[i])

		self._aim.draw(System().get_mouse_position())
		self._hud.draw(lives=self._lives, score=self._score)

	def on_mouse_event(self, position, button, pressed):
		if pressed and button == BUTTON_LEFT:
			self._shoot_sound.play()
		
			for i, bandit in enumerate(self._bandits):
				if bandit is not None:
					if bandit.is_inside_hitbox(self.SPAWNABLE_POSITIONS[i], position):
						bandit.on_being_shot()
						break
						
	def on_update(self, dt):
		self._spawn_timer.advance(dt)
		self._spawn_timer.fuse *= 1 - self.SPAWN_RATE_INCREASE * dt

		for i, bandit in enumerate(self._bandits):
			if bandit is not None:
				bandit.on_update(dt)

		if self._lives <= 0:
			HighscoresFile.write('Wild West', self._score)
			System().set_mouse_visibility(True)
			System().current_stage = GameOverStage(self._score)

	def on_key_event(self, key, pressed):
		if pressed and key == K_ESCAPE:
			System().set_mouse_visibility(True)
			System().current_stage = PausedStage(self)

	def spawn_bandit_randomly(self):
		free = [i for i in range(len(self._bandits)) if self._bandits[i] is None]
		
		if len(free) > 0:
			position = random.choice(free)

			self._bandits[position] = random.choice(self.BANDIT_TYPES)()
