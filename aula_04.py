# AULA 04 - HERANÇA
import aula_03  ## importando as classes no arquivo da aula 3


class Carro(aula_03.VeiculoVeiculo):
    """
    => instanciando a classe carro que herda de Veiculos no arquivo aula_3;
    => Nos atributos da classe utilizar arquivo.nome_da_classe;
    => HERANÇA MULTIPLA - Tem como você herdar de mais de uma classe, mais não
        é recomendado que isso aconteça pois o codigo pode virar uma bagunça;
    """

    def __init__(self, cor, tipo_combustivel, potencia, qtd_combustivel, qtd_portas):
        """
        => O metodo recebe todos os argumentos da classe pai;
        => Os argumentos devem ser passados na ordem do construtor filho;
        """
        super().__init__(cor, tipo_combustivel, potencia, qtd_combustivel)
        self.qtd_portas = qtd_portas

    def abastecer(self, qtd_combustivel):
        print("Acessando a função atravez da classe moto.")
        if self.qtd_combustivel > 30:
            print("O tanque da moto ja esta cheio!")
        else:
            self.qtd_combustivel += qtd_combustivel


class Moto(aula_03.VeiculoVeiculo):
    """
    => instanciando a classe carro que herda de Veiculos no arquivo aula_3;
    => Nos atributos da classe utilizar arquivo.nome_da_classe;
    """

    def __init__(self, cor, tipo_combustivel, potencia, qtd_combustivel, qtd_lugares):
        """
        => O metodo recebe todos os argumentos da classe pai;
        => Os argumentos devem ser passados na ordem do construtor filho;
        """
        super().__init__(cor, tipo_combustivel, potencia, qtd_combustivel)
        self.qtd_lugares = qtd_lugares

        """
        POLIMORFISMO
        => DESCRIÇÃO: É a capacidade de sobrescrever um metodo existente na classe pai;
        => O polimorfismo nos ajuda a adaptar o metodo existente na classe pai para que ele
            possa ser usado de maneira correta.
        """

    ## APLICANDO POLIMORFISMO
    def abastecer(self, qtd_combustivel):
        print("Acessando a função atravez da classe carro.")

        if self.qtd_combustivel > 140:
            print("O tanque esta cheio!!")
        else:
            self.qtd_combustivel += qtd_combustivel
