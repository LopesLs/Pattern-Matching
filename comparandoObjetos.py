class Pessoa:
    __match_args__ = ('nome', 'idade')
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

def buscainfo(pessoa : Pessoa):
    match pessoa:
        case Pessoa('Carlos' | 'Michel'):
            return 'Programa em python'
        case Pessoa(_, _) as alguem if alguem.idade > 18:
            return f'O nome é {alguem.nome} é maior que 18 anos'

print(buscainfo(
    Pessoa('Jarbas', 67)
))