from objeto import Objeto


class BGElement(Objeto):

    # (115, 53), (223, 53)
    # (115, 239), (223, 239)
    # + offset do tamanho

    def __init__(self,
                 posicao: list,
                 anim: object):
        super().__init__(posicao, anim)
        self.img_atual = self.anim[0]
        self.rect = self.img_atual.get_rect()
        self.pos_inicial()

    def update(self):
        self.rect.y += self.velocidade_controller.vel_atual
        if (self.rect.top >= self.tela.height):
            self.rect.bottom = 0
