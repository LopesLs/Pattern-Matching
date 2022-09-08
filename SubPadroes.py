# Cria uma estrutura Match Case Pattern onde você vai fazer uma verificação se o nome é Carlos ou Emanuel, se não for nenhum dos dois então mostre que são pessoas comuns.

info = ['Bobby Fischer', 18]

match info:
    case ['Carlos' | 'Emanuell', _]:
        print('É um dos monitores')
    case []:
        print('Não foi informado nada')
    case _:
        print('Só uma pessoa comum')