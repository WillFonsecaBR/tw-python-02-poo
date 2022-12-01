# AULA 05 - ATRIBUTOS DE VISIBILIDADE E ENCAPSULAMENTO
class Veiculo():
    """
    ATRIBUTOS PUBLICOS => Podem ser acessados de qualquer lugar do software, modificados por qualquer medodo;
    ATRIBUTOS PRIVADOS => So podem ser acessado por sua propria classe via metodos;
    ATRIBUTOS PROTEGIDOS => Somente classes filhas podem alterar o conteudo;
    """
    def __init__(self, cor, tipo_combustivel, potencia, libras_pneus):
        # ALTERANDO OS ATRIBUTOS PARA PRIVATE
        self.__cor = cor # PRIVATE
        self.__tipo_combustivel = tipo_combustivel # PRIVATE
        self.__potencia = potencia # PRIVATE
        self._qtd_combustivel = 0 # PROTECT
        self.__is_ligado = False # PRIVATE
        self.__velocidade = 0 # PRIVATE
        self._libras_pneus = libras_pneus # ATRIBUTO PROTECT

    """
    ENCAPSULAMENTO => Aplicar as regras aos atributos, fazendo isso criar os metodos que 
    irão modificar estes atributos.
    """
    def __del__(self):
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


### ===============================================================
### DEFININDO NOVOS METODOS PARA ALTERAR AS PROPRIEDADES
    """
    PROPERTYS => As propertys servem para criar funções de modificação ou acesso
                as propriedades de determinada classe;
    """
    @property
    def cor (self):
        """
        EXEMPLO 1 => Neste exemplo temos somente o acesso ao valor do atributo cor;
        """
        return self.__cor

    @property
    def tipo_combustive(self):
        return  self.tipo_combustive

    @property
    def potencia(self):
        return self.__potencia

    @property
    def qtd_combustivel(self):
        """
        EXEMPLO 2 => Neste exemplo temos o acesso ao valor do atributo e
                    algumas tomadas de decisões que enviam uma mensagem ou o
                    resultado do atributo qtd_combustivel;
        """
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


