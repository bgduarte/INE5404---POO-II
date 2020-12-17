import pygame, os, math, collections, numbers, abc
from pygame.locals import *

#------------------------------------------------------------------------------#

pygame.init()
pygame.mixer.init()
pygame.font.init()

#------------------------------------------------------------------------------#

class Point:
	def __init__(self, x, y=None):
		if isinstance(x, collections.abc.Container):
			self.x, self.y = x
		else:
			self.x = x
			self.y = y

	def __add__(a, b):
		if isinstance(b, Point):
			return Point(a.x + b.x, a.y + b.y)

		else:
			raise TypeError("unsupported operand type(s) for +: %r and %r"
								 % (type(a).__name__, type(b).__name__))

	def __str__(self):
		return '(%f, %f)' % (self.x, self.y)

	def __sub__(a, b):
		if isinstance(b, Point):
			return Point(a.x - b.x, a.y - b.y)
		
		else:
			raise TypeError("unsupported operand type(s) for -: %r and %r"
								 % (type(a).__name__, type(b).__name__))

	def __truediv__(a, b):
		if isinstance(b, Point):
			return Point(a.x / b.x, a.y / b.y)

		elif isinstance(b, numbers.Number):
			return Point(a.x / b, a.y / b)
		
		else:
			raise TypeError("unsupported operand type(s) for /: %r and %r"
								 % (type(a).__name__, type(b).__name__))

	def angle(self):
		return math.degrees(math.atan2(self.y, self.x))

	def distance_to_line(p0, p1, p2):
		nominator = abs((p1.y - p2.y) * p0.x + 
							 (p2.x - p1.x) * p0.y + 
							 (p1.x * p2.y - p2.x * p1.y))
		
		denominator = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

		return nominator / denominator

	def rotate(self, angle):
		cos = math.cos(math.radians(angle))
		sin = math.sin(math.radians(angle))

		return Point(self.x * cos - self.y * sin, self.x * sin + self.y * cos)

	def to_tuple(self):
		return (self.x, self.y)

#------------------------------------------------------------------------------#

class Stage(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def __init__(self):
		pass

	def on_draw(self, dt):
		pass

	def on_update(self, dt):
		pass

	def on_key_event(self, key, pressed):
		pass

	def on_mouse_event(self, position, button, pressed):
		pass

#------------------------------------------------------------------------------#

class Timer:
	def __init__(self, fuse, function=None, repeat=False):
		self.fuse = fuse

		self._elapsed  = 0
		self._function = function
		self._repeat   = repeat
	
	def advance(self, time):
		self._elapsed += time

		if self.is_done():
			if self._repeat:
				self._elapsed = 0

			if self._function:
				self._function()
	
	def is_done(self):
		return self._elapsed >= self.fuse

	def reset(self):
		self._elapsed = 0

#------------------------------------------------------------------------------#

class Singleton(type):
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super().__call__(*args, **kwargs)

		return cls._instances[cls]

#------------------------------------------------------------------------------#

class System(metaclass=Singleton):
	def __init__(self):
		self._working_path  = os.getcwd().replace('\\', '/') + '/'
		
		self._current_stage = None
		self._default_stage = None
	
		self._screen = None
		self._window = None

	@property
	def current_stage(self):
		return self._current_stage

	@current_stage.setter
	def current_stage(self, value):
		self._current_stage = value or self._default_stage()

	def draw(self, surface, point, angle=0, pivot=None):
		pivot = pivot or Point(surface.get_size())/2

		if angle:
			angle %= 360

			width, height = surface.get_size()
			sin, cos = math.sin(math.radians(angle)), math.cos(math.radians(angle))
			min_pos = Point(
				min(0, sin * height, cos * width, sin * height + cos * width),
				max(0, sin * width, -cos * height, sin * width - cos * height)
			)

			offset         = Point(pivot.x, -pivot.y)
			offset_rotated = offset.rotate(angle)
			offset_delta   = offset_rotated - offset

			origin = (point.x - pivot.x + min_pos.x - offset_delta.x,
						 point.y - pivot.y - min_pos.y + offset_delta.y)

			self._screen.blit(pygame.transform.rotate(surface, angle), origin)

		else:
			self._screen.blit(surface, (point - pivot).to_tuple())

	def get_screen_size(self):
		return self._screen.get_size()

	def get_mouse_position(self):
		scaling = self._window.get_size()[0] / self._screen.get_size()[0]

		return Point(pygame.mouse.get_pos()) / scaling

	def set_mouse_visibility(self, visible):
		pygame.mouse.set_visible(visible)

	def setup(self, title, width, height, scaling=1):
		pygame.display.set_caption(title)

		self._window = pygame.display.set_mode((width, height))
		self._screen = pygame.Surface((width / scaling, height / scaling))

	def start(self, default_stage):
		self._default_stage = default_stage
		self.current_stage  = self._default_stage()

		clock   = pygame.time.Clock()
		running = True

		while running:
			dt = clock.tick(60)

			for event in pygame.event.get():
				if event.type == QUIT:
					running = False
				
				elif event.type == KEYDOWN:
					self.current_stage.on_key_event(event.key, 1)
				
				elif event.type == KEYUP:
					self.current_stage.on_key_event(event.key, 0)

				elif event.type == MOUSEBUTTONDOWN:
					self.current_stage.on_mouse_event(self.get_mouse_position(), 
																 event.button, 1)

				elif event.type == MOUSEBUTTONUP:
					self.current_stage.on_mouse_event(self.get_mouse_position(), 
																 event.button, 0)
		
			self.current_stage.on_draw(dt/1000)
			self.current_stage.on_update(dt/1000)

			scaled = pygame.transform.scale(self._screen, self._window.get_size())
	
			self._window.blit(scaled, (0, 0))
			pygame.display.flip()
		
		pygame.quit()

	@property
	def working_path(self):
		return self._working_path

#------------------------------------------------------------------------------#

class Text:
	def __init__(self, path, size, color=None):
		self._font     = pygame.font.Font(System().working_path + path, size)
		self._contents = ''
		self._color    = color or (255, 255, 255)
		self._surface  = None

	def draw(self, point):
		if self._surface:
			width, _ = self._font.size(self._contents)

			System().draw(self._surface, point + Point(width/2, 0))

	@property
	def contents(self):
		return self._contents

	@contents.setter
	def contents(self, value):
		if value != self._contents:
			self._contents = value
			self._surface  = self._font.render(self._contents, True, self._color)

#------------------------------------------------------------------------------#

class Image:
	_cache = {}

	def __init__(self, path, pivot=None):
		if path not in self._cache:
			self._cache[path] = pygame.image.load(System().working_path + path) \
													  .convert_alpha()

		self._surface = self._cache[path]
		self._pivot   = pivot

	@property
	def dimensions(self):
		return self._surface.get_size()

	def draw(self, point, angle=0):
		System().draw(self._surface, point, angle, self._pivot)

	@property
	def height(self):
		return self.dimensions[1]

	@property
	def width(self):
		return self.dimensions[0]

#------------------------------------------------------------------------------#

class GameObject(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def __init__(self, position=None, rotation=0):
		self.position = position or Point(0, 0)
		self.rotation = rotation

	@property
	def rotation(self):
		return self._rotation

	@rotation.setter
	def rotation(self, angle):
		self._rotation = angle % 360