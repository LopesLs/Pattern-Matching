# 2. Elabore um  programa em linguagem Python que tem como saída o nome do  time vencedor de uma partida de futebol.O seu programa deve receber os nomes dos dois times da partida e o número de gols marcados por cada um deles. Vence a partida aquele time que marcar o maior número de gols. Exiba a mensagem “EMPATE”, caso a partida não tenha tido um vencedor.

# Conhecimentos Utilizados;
# - Funções
# - Pattern Matching
# - Type Hints
# - POO
# - Operadores Ternários


# Paradigma de programação
def calculavencedor(time1 : str, gols1 : int, time2 : str, gols2 : int) -> str:
    match gols1:
        case quantidadegols if quantidadegols > gols2:
            return f'\n{time1} foi o vencedor por {quantidadegols}x{gols2}, jogão' if quantidadegols < 4 else f'\n{time1} foi o vencedor por {quantidadegols}x{gols2}, goleadaa'
        case quantidadegols if quantidadegols < gols2:
            return f'\n{time2} foi o vencedor por {gols2}x{quantidadegols}, acirrado a disputa' if gols2 < 4 else f'\n{time2} ganhou o jogo por {gols2}x{quantidadegols}, passou por cima'
        case _:
            return f'\nEMPATE!, o jogo saiu de {quantidadegols}x{gols2}'

#print(calculavencedor(input('Informe o nome do time da casa: '), int(input('Informe os gols do time da casa: ')), input('\nInforme o nome do time de fora: '), int(input('Informe a quantidade de gols do time de fora: '))))

# Paradigma Orientado a Objetos
class CampNoul():
    def __init__(self, casa : str, golscasa : int, fora : str, golsfora : int) -> None:
        self.timedacasa = casa
        self.golsdacasa = golscasa
        self.timedefora = fora
        self.golsdefora = golsfora
    
    def buscavencedor(self) -> str:
        match self.golsdacasa:
            case quantidadegols if quantidadegols > self.golsdefora:
                return f'\n{self.timedacasa} foi o vencedor por {quantidadegols}x{self.golsdefora}, jogão' if quantidadegols < 4 else f'\n{self.timedacasa} foi o vencedor por {quantidadegols}x{self.golsdefora}, goleadaa'
            case quantidadegols if quantidadegols < self.golsdefora:
                return f'\n{self.timedefora} foi o vencedor por {self.golsdefora}x{quantidadegols}, acirrado a disputa' if self.golsdefora < 4 else f'\n{self.timedefora} ganhou o jogo por {self.golsdefora}x{quantidadegols}, passou por cima'
            case _:
                return f'\nEMPATE!, o jogo saiu de {quantidadegols}x{self.golsdefora}'

estadio = CampNoul(input('Informe o nome do time da casa: '), int(input('Informe os gols do time da casa: ')), input('\nInforme o nome do time de fora: '), int(input('Informe a quantidade de gols do time de fora: ')))
print(estadio.buscavencedor())
