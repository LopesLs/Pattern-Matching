# 1. Criando um match case pattern que verifica as cores e para cada uma dá a sua opinião.

def chatodascores(rgb):
    match rgb:
        case r , g, b if r == 255 and g == 255 and b == 255:
            print('Branco e eu não gosto da cor branca')
        case r, g, b if r == 255:
            print('Muito vermelho irmãozinho')
        case r, g, b if g == 255:
            print('Eu amo a natureza, mas tá muito verde')
        case r, g, b if b == 255:
            print('Tá muito azul, recomendo baixar urgente')
        case _:
            print('Isso ficou realmente bom')

chatodascores((22, 255, 25)) # Eu amo a natureza, mas tá muito verde