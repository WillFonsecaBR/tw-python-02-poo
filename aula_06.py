### AULA 06 - CLASSES ABSTRATAS E BIBLIOTECA ABC
"""
ABSTRACT CLASS => Uma classe abstrata não pode ser instanciada, ela deve servir de
                base para outras classes filhas, então ela pode ser acessadas extritamente
                pela classe filha.

ABSTRACT METHOD => Um metodo abstrato em uma classe qualquer deve ser sobrescrito na classe
                filha. Esse metodo deve se comportar de maneira diferente do metodo da classe pai
                garantindo que a classe filha crie uma nova linha de raciocinio na função.
                OBS: Se o metodo não for implementado ele vai sempre se conportar como o da classe pai.

PYTHON E ABSTRACT => O python não tem a funcionalidade de abstração por padrão, por isso é
                    usado uma biblioteca chamada ABC, com essa biblioteca conseguimos fazer com que
                    o python entenda metodos e classes como abstratas usando anotação de propertys.
"""

### ORGANIZANDO O CODIGO DA AULA 5
import abc
class Veiculo(abc.ABC):
    """
    OBSERVAÇÕES 1 => Para fazer com que a classe seja abstrata basta passar a notação
                    "abc.ABC";
    OBSERVAÇÕES 2 => Quando a classe é abstrata todos os metodos abstratos contidos nela
                    devem ser sobrescritos na classe filha;
    OBSERVAÇÕES 2 => Todos os metodos não abstratos tambem podem ser sobrescrito normalmente
                    em qualquer classe filha;
    """
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

    @abc.abstractmethod
    def pintar(self, cor):
        """
        EXEMPLO 1 => A partir da notação @abc.abstractmethod o metodo pintar se torna
                    abstrato e pode ser implementado nas classes filhas;
        """
        self.__cor = cor

    def __del__(self): # APAGA TODOS OS DADOS DE TODOS OS OBJETOS
        print("O objeto foi removido do sistema!")

    def abastecer(self, qtd_combustivel):
        self._qtd_combustivel += qtd_combustivel

    @abc.abstractmethod
    def ligar(self):
        """
        EXEMPLO 2 => Agora o metodo ligado tambem é abstrato e pode ser alterado;
        """
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
        """
        EXEMPLO 1 - Sobrescrevendo metodo pintar
        """
        if cor == "preto":
            print("Não trabalhamos com carro preto!")
        else:
            self._cor = cor
    def ligar(self):
        """
        EXEMPLO 2 - Sobrescrevendo metodo ligar
        """
        self.is_ligado = True

    def desligar(self):
        super().desligar()
        """
        EXEMPLO 3 - Sobrescrevendo um metodo que não é abstrato
        """
        if self.__is_ligado == True:
            self.__is_ligado = False
        else:
            print("O carro já esta desligado!")

