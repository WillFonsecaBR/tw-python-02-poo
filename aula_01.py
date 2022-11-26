# AULA 01 - ESCOPOS E NAMESPACES

## Importando namespaces

# from nome_do_modulo import * => Importa tudo

# from nome_do_modulo import metodo_a, metodo_b => Importa somente os modulos escolhidos

# import nome_do_modulo => Mais utilizada, você deve usar o nome da biblioteca.

# CTRL + BACKSPACE => mostra as funções dentros dos modulos


import math # MODO CORRETO DE IMPORTAR

print(math.isqrt(20)) # chamando uma função do modulo

## Resolução de escopo

nome = "João" #escopo global

def funcao():
  nome = "José" #escopo local
