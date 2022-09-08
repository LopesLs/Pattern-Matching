# 1. Criando um exemplo literal do status de um site

def http_error(status : int) -> str:
    match status:
        case 404:
            return 'Inexistente'
        case 401:
            return 'Sem autorização'
        case 403:
            return 'Proíbido'
        case 418:
            return 'Você pode'
        case _:
            return 'Sua internet é ruim, aceite'

print(http_error(404)) # Inexistente

# 2. Criando um match case pattern literal que verifica se os valores de uma lista são 1 2 e 3 e o tamanho de elementos igual a 3.

def fiscaldelista(lista : list):
    match lista:
        case [1, 2, 3]:
            return 'len(lista) = 3 e os valores são respectivamente (1, 2, 3) ou pode estar vazia'
        case _:
            return 'Péssima lista, os elementos não são (1, 2, 3) respectivamente.'

print(fiscaldelista([4])) # Péssima lista, os elementos não são (1, 2, 3) respectivamente

# 3. Criando um match case pattern não tão literal assim que verifica se o primeiro elemento da lista é igual á 1, se o segundo elemento é igual a 2 e se o terceiro elemento é igual a 3 desde que o len de lista seja igual a 3.

def primodofiscal(lista : list):
    match lista:
        case [1, _, _]:
            return 'len(lista) = 3 e o primeiro elemento é igual a 1'
        case [_, 2, _]:
            return 'len(lista) = 3 e o segundo elemento é igual a 2'
        case[_, _, 3]:
            return 'len(lista) = 3 e o terceiro elemento é iguak a 3'
        case[]:
            return 'Porque uma lista vazia!?'
        case _:
            return 'Isso não se encaixa nos meus cases sua lista é ruim'

print(primodofiscal([])) # Porque uma lista vazia!?

# Criando um match case pattern não tão literal assim que verifica se o primeiro elemento de uma lista é igual a 1, 2 ou tres não importa o tamanho da lista

def irmaodofiscal(lista : list):
    match lista:
        case [1, *restolista]:
            return f'O primeiro elemento é 1 {restolista = }'
        
        case[2, *restolista]:
            return f'O primeiro elemento é 2 {restolista = }'

        case [3, *restolista]:
            return f'O primeiro elemento é 3 {restolista = }'
        
        case [_, *restolista]:
            return f'O primeiro elemento não esta entre (1, 2, 3) {restolista = }'

print(irmaodofiscal([1, 4, 6, 7])) # O primeiro elemento é 1 restolista = [4, 6, 7]
