#Em situações normais esse essa exceção não deve ser levantada,
#porém ela facilita a debugar o código caso algo dê errado
class TipoNaoCompativelException(Exception):
    def __init__(self):
        super().__init__("O tipo que você está tentando inserir na lista não é suportado")
