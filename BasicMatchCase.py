# 1. Criando um código com if para verificar se um valor qualquer pode ser 1 ou 2.

def verifica(x : float) -> str:
    if x == 1:
        return ('O valor é igual a 1 COM IF')
    elif x == 2:
        return ('O valor é igual a 2 COM IF')
    else:
        return (f'O valor não é 1 nem 2, {x = } COM IF')

print(verifica(2)) # O valor é igual a 2 COM IF
print(verifica(5)) # O valor não é 1 nem 2, x = 5 COM IF

# 2. Criando um código utilizando match case para verificar se um valor qualquer pode ser 1 ou 2

def search(x : float) -> str:
    match x:
        case 1:
            return 'O valor é igual a 1 COM MATCH CASE'
        case 2:
            return 'O valor é igual a 2 COM MATCH CASE'
        case _:
            return f'O valor não é 1 nem 2, {x = } COM MATCH CASE'

print(search(2)) # O valor é igual a 2 COM MATCH CASE
print(search(5)) # O valor não é 1 nem 2, x = 5 COM MATCH CASE