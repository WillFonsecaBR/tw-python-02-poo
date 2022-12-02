# AULA 0 - PSEUDO INTERFACES
"""
INTERFACES => O python não tem uma nomeclatura ou tipo para criar uma classe abstrata, é
            utilizado um conceito chamado pseudo abstrato onde é criado uma classe com todos
            os metodos que são de obrigatoriedade de implementação. Todos os metodos da classe
            deve ser abstrato.
DUCK-TYPING => É uma forma de verificar interfaces (Não entendi direito, cou ter que pesquisar)
"""
### ORGANIZANDO O CODIGO DA AULA 5
import abc

class Interface_veiculo(abc.ABC):
    """
    EXEMPLO 1 => Essa classe implementa todos os metodos que são abstratos, criando assim
                a classe abstrata.
    """
    @abc.abstractmethod
    def pintar(self, cor):
        pass # SERA IMPLEMENTADO NA CLASSE PAI

    @abc.abstractmethod
    def abastecer(self, qtd_combustivel):
        pass # SERA IMPLEMENTADO NA CLASSE PAI

    @abc.abstractmethod
    def ligar(self):
        pass # SERA IMPLEMENTADO NA CLASSE PAI

    @abc.abstractmethod
    def desligar(self):
        pass # SERA IMPLEMENTADO NA CLASSE PAI

    @abc.abstractmethod
    def acelerar(self, velocidade):
        pass # SERA IMPLEMENTADO NA CLASSE PAI

class Veiculo(Interface_veiculo, abc.ABC):
    def __init__(self, cor, tipo_combustivel, potencia, libras_pneus):
        self.__cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0
        self.__is_ligado = False
        self.__velocidade = 0
        self._libras_pneus = libras_pneus

    @property
    def cor (self):
        return self.__cor

    @property
    def tipo_combustive(self):
        return  self.tipo_combustive

    @property
    def potencia(self):
        return self.__potencia

    @property
    def qtd_combustivel(self):
        if self._qtd_combustivel > 0:
            print("O tanque esta vazio!")
        else:
            return self._qtd_combustivel

    @property
    def is_ligado(self):
        if self.is_ligado == True:
            print("O carro esta ligado.")
        else:
            print("O carro esta desligado.")

    @property
    def velocidade(self):
        if self.__velocidade > 0:
            print(F"A sua velocidade é: {self.__velocidade}")
        else:
            print("O carro esta parado!!")
    @property
    def libras_pneus(self):
        return self._libras_pneus

    """
    OBSERVAÇÕES 01 => Todos os metodos abstratos devem ser implementados;
    OBSERVAÇÕES 02 => Os metodos que não forem implementados nas classes 
                    pai devem ser implementados nas classes filhas obrigatoriamente;
    """
    def pintar(self, cor):
        self.__cor = cor

    def __del__(self): # APAGA TODOS OS DADOS DE TODOS OS OBJETOS
        print("O objeto foi removido do sistema!")

    def abastecer(self, qtd_combustivel):
        self._qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.__is_ligado == True:
            print("O carro já esta ligado!")
        else:
            self.__is_ligado = True

    def desligar(self):
        self.__is_ligado = False

    def acelerar(self, velocidade):
        if self._qtd_combustivel > 0:
            print(f"O carro esta sem combustível!")
        elif self.__is_ligado == False:
            print("O carro esta desligado!")
        else:
            self.__velocidade += velocidade
            print("O carro foi ligado!!")


### UTILIZANDO CODIGO DA AULA 3

class Carro(Veiculo):
    def __init__(self, __cor, __tipo_combustivel, __potencia, __qtd_combustivel, qtd_portas):
        super().__init__(__cor, __tipo_combustivel, __potencia, __qtd_combustivel)
        self.qtd_portas = qtd_portas

    def abastecer(self, qtd_combustivel):
        print("Acessando a função atravez da classe moto.")
        if self.qtd_combustivel > 30:
            print("O tanque da moto ja esta cheio!")
        else:
            self.__qtd_combustivel += qtd_combustivel

    def pintar(self, cor):
        if cor == "preto":
            print("Não trabalhamos com carro preto!")
        else:
            self._cor = cor
    def ligar(self):
        self.is_ligado = True

    def desligar(self):
        super().desligar()
        if self.__is_ligado == True:
            self.__is_ligado = False
        else:
            print("O carro já esta desligado!")

