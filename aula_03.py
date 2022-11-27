# AULA 03 - CONSTRUTORES E DESTRUTORES

class Carro():
    ## FUNÇÃO CONSTRUTORA
    def __init__(self, cor, qtd_portas, tipo_combustivel, potencia):
        self.cor = cor;
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = 0  ## INICIANDO OBJETO PREENCHIDO
        self.is_ligado = False  ## INICIANDO OBJETO PREENCHIDO
        self.velocidade = 0  ## INICIANDO OBJETO PREENCHIDO

    ## FUNÇÃO DESTRUTOR
    def __del__(self):
        print("O objeto foi removido do sistema!")
        """
        para apagar o objeto no codigo:
        dell nome_do_objeto
        """

    def abastecer(self, qtd_combustivel):
        self.qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.is_ligado == True:
            print("O carro já esta ligado!")
        else:
            self.is_ligado = True

    def desligar(self):
        self.is_ligado = False

    def acelerar(self, velocidade=10):  # velocidade=10 é um valor padrão.
        if self.qtd_combustivel > 0:
            print(f"O carro esta sem combustível!")
        elif self.is_ligado == False:
            print("O carro esta desligado!")
        else:
            self.velocidade += velocidade


### ===================================================================================

## PARA UTILIZAR NA AULA 4
class Veiculo():
    def __init__(self, cor, tipo_combustivel, potencia):
        self.cor = cor;
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = 0
        self.is_ligado = False
        self.velocidade = 0

    def __del__(self):
        print("O objeto foi removido do sistema!")
        """
        para apagar o objeto no codigo:
        dell nome_do_objeto
        """

    def abastecer(self, qtd_combustivel):
        self.qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.is_ligado == True:
            print("O carro já esta ligado!")
        else:
            self.is_ligado = True

    def desligar(self):
        self.is_ligado = False

    def acelerar(self, velocidade=10):  # velocidade=10 é um valor padrão.
        if self.qtd_combustivel > 0:
            print(f"O carro esta sem combustível!")
        elif self.is_ligado == False:
            print("O carro esta desligado!")
        else:
            self.velocidade += velocidade
            print("O carro foi ligado!!")
