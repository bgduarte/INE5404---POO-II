from game import System

System().setup(title='Minigamer2000', width=800, height=600, scaling=2)

from stages.mainmenu import MainMenuStage

# Esse é o entry point do jogo.
#
# Algumas considerações:
#
# - Variaveis privadas não são definidas com dunderscore (__) pois name mangling
#   foi implementado para previnir conflitos de nome por herança, não para
#   permitir membros privados
#   (https://docs.python.org/3/tutorial/classes.html#private-variables)
#
# - Campos publicos não são sempre encapsulados com getters e setters pois caso
#   seja necessario no futuro, basta apenas esconder o campo e usar os
#   decorators @property e #xxx.setter

System().start(default_stage=MainMenuStage)