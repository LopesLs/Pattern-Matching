# 1. Criando uma estrutura match case pattern que simula as cores do rgb o match deve nomear os parâmetros e imprimir cada um deles.

def descrevendorgb(rgb):
    match rgb:
        case r, g, b: # Executa quando len(rgb) == 3
            print(f'O parâmetro red possui {r = }')
            print(f'O parâmetro green possui {g = }')
            print(f'O parâmtero blue possui {b = }')

descrevendorgb((255, 255, 255)) # Chamando a função

def descrevendorgba(rgba):
    match rgba:
        case r, g, b: # Executa quando len(rgba == 3)
            print('Mas ué, cadê o alpha?')
        case r, g, b, a: # Executa quando len(rgba == 4)
            print(f'O parâmetro red possui {r = }')
            print(f'O parâmetro green possui {g = }')
            print(f'O parâmetro blue possui {b = }')
            print(f'O parâmetro alpha possui {a = }')

descrevendorgba((255, 255, 255)) # Chamando a função

# 2. Criando um match case pattern que determina qual acao devo tomar baseando na entrada de dados

def movimentacao(caminho):
    match caminho.split():
        case [acao] if acao == 'direita' or acao == 'esquerda' or acao == 'cima' or acao == 'baixo':
            print('Você tem que falar a ação antes')
        case ['mover']:
            print('Para onde quer ir?')
        case 'mover', 'direita' | 'esquerda' as direcao:
            print(f'Você se moveu horizontalmente para {direcao}')    
        case 'mover', 'cima' | 'baixo' as direcao:
            print(f'Você se moveu verticalmente para {direcao}')
        case _:
            print(f'Não entendi o seu movimento')

movimentacao('nada')
