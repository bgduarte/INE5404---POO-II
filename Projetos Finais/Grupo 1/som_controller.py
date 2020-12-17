from volume_dao import VolumeDAO
from singleton import Singleton
import pygame


class SomController(metaclass=Singleton):
    def __init__(self):
        self.__volume_dao = VolumeDAO()
        if len(self.__volume_dao.get_all()) == 0:
            self.__volume_dao.set_volume_padrao()
        self.__volume_atual_music = self.__volume_dao.get_volume_music()
        self.__volume_atual_sound = self.__volume_dao.get_volume_sound()
        
        #Inicializa sons
        #Obstaculos
        self.__tosse = pygame.mixer.Sound("Materials/tosse.mp3")
        self.__tosse.set_volume(self.__volume_atual_sound)
        self.__respiracao = pygame.mixer.Sound("Materials/respiracao.mp3")
        self.__respiracao.set_volume(self.__volume_atual_sound)
        #Efeitos
        self.__sound_efeito = pygame.mixer.Sound("Materials/efeito.mp3")
        self.__sound_efeito.set_volume(self.__volume_atual_sound)
        self.__gripezinha = pygame.mixer.Sound("Materials/gripezinha.mp3")
        self.__gripezinha.set_volume(self.__volume_atual_sound)

        #Listas com os sons
        self.__sounds_obstaculos = [self.__tosse, self.__respiracao]
        self.__sounds_efeitos = [self.__sound_efeito, self.__gripezinha]

        #Inicializa as musicas de fundo
        self.__jogando_music = "Materials/background.mp3"
        self.__derrota_music = "Materials/death.mp3"

        #Lista com as musicas de fundo
        self.__musics = [self.__jogando_music, self.__derrota_music]
        
    #Toca um som da lista pelo index
    def play_sound_obstaculos(self, index):
        self.set_volume_sounds(self.__volume_atual_sound)
        self.__sounds_obstaculos[index].play()

    #Toca um som da lista pelo index
    def play_sound_efeitos(self, index):
        self.set_volume_sounds(self.__volume_atual_sound)
        self.__sounds_efeitos[index].play()

    #Toca uma musica
    def play_music(self,index):
        pygame.mixer.music.load(self.__musics[index])
        self.set_volume_music(self.__volume_atual_music)
        pygame.mixer.music.play(-1)

    #Pausa a musica
    def pause_music(self):
        pygame.mixer.music.pause()

    #Despausa a musica
    def unpause_music(self):
        pygame.mixer.music.unpause()

    #Para a musica atual
    def stop_music(self):
        pygame.mixer.music.stop()

    #Volume tem que ser float de 0 a 1
    def set_volume_music(self, volume):
        self.__volume_dao.set_volume_music(volume)
        self.update_volume()
        pygame.mixer.music.set_volume(self.__volume_atual_music)

    #Volume tem que ser float de 0 a 1
    def set_volume_sounds(self, volume):
        self.__volume_dao.set_volume_sound(volume)
        self.update_volume()
        for sound in self.__sounds_obstaculos:
            sound.set_volume(self.__volume_atual_sound)
        for sound in self.__sounds_efeitos:
            sound.set_volume(self.__volume_atual_sound)

    #Retorna ao volume padrão (0.5)
    def set_volume_padrao(self):
        self.__volume_dao.set_volume_padrao()
        self.update_volume()

    #Atualiza o volume atual
    def update_volume(self):
        self.__volume_atual_music = self.__volume_dao.get_volume_music()
        self.__volume_atual_sound = self.__volume_dao.get_volume_sound()

    @property 
    def sounds_obstaculos(self):
        return self.__sounds_obstaculos

    @property
    def sounds_efeitos(self):
        return self.__sounds_efeitos
    
    @property
    def musics(self):
        return self.__musics

    @property
    def volume_atual_music(self):
        return self.__volume_atual_music

    @property
    def volume_atual_sound(self):
        return self.__volume_atual_sound
