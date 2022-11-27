# AULA 02 - CLASSES E OBJETOS

### Criando uma nova classe
class Carro():
    """DOCSTRING: a DOCSTRING É UTILIZADA PARA DESCREVER CLASSES E METODOS FACILITANDO O ENTENDIMENTO DOS MESMOS"""
    """EXEMPLO DE DOCSTRING GERAL"""

    # Atributos da classe
    def __init__(self, cor, qtd_portas, tipo_combustivel, potencia, qtd_combustivel, is_ligado, velocidade):
        """DOCSTRING: Exemplo de docstring dos atributos da classe"""
        self.velocidade = velocidade
        self.cor = cor;
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = qtd_combustivel
        self.is_ligado = is_ligado

    ## Metodos da classe
    def abastecer(self, qtd_combustivel):

        self.qtd_combustivel += qtd_combustivel

    def ligar(self):
        """DOCSTRING: Exemplo de docstring da classe ligar"""
        if self.is_ligado == True:
            print("O carro já esta ligado!")
        else:
            self.is_ligado = True

    def desligar(self):
        """DOCSTRING: Exemplo de docstring da classe desligar"""
        self.is_ligado = False

    def acelerar(self, velocidade=10):  # velocidade=10 é um valor padrão.
        if self.qtd_combustivel > 0:
            print(f"O carro esta sem combustível!")
        elif self.is_ligado == False:
            print("O carro esta desligado!")
        else:
            self.velocidade += velocidade


"""
Para recorrer a docstring de qualquer metodo ou classe basta chamar o metodo ou classe
utilizando o atributo help

help(INSTANCIA.CLASSE/METODO) 

Depois é só rodar o codigo
"""
