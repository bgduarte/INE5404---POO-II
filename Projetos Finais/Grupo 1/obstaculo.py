from objeto import Objeto


class Obstaculo(Objeto):
    def __init__(self, posicao, anim):
        super().__init__(posicao, anim)
        self.img_atual = self.anim[0]
        self.rect = self.img_atual.get_rect()
        self.pos_inicial()
        self.spriteNum = 0
        self.spriteNumMax = len(self.anim)
        self.spriteTimer = 0
        self.spriteTimerMax = 4

    def update(self):
        self.rect.y += self.velocidade_controller.vel_atual
        if (self.rect.top >= self.tela.height):
            self.kill()
            del self
