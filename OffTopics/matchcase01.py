# 1. Desenvolva um programa em linguagem python que solicita do usuário um número real e verifica se esse número é maior ou menor que 0. Utilize Match Pattern

# Conhecimentos Utilizados;
# - Funções
# - Pattern Matching
# - Type Hints
# - POO

# Paradigma Estrutural
def maiormenor(numeroreal : float) -> str:
    match numeroreal:
        case numero if numero > 0: # Usando um Guarda para verificar
            return 'O número é maior que 0'
        case numero if numero < 0:
            return 'O número é menor que 0'
        case _:
            return 'O número é igual a 0'

# Paradigma Orientado a objeto
class AnalisaNumero():
    def __init__(self, real : float) -> None:
        self.numero = real
        return None
    
    def Analisa(self) -> str:
        match self.numero:
            case numero if numero > 0:
                return f'{numero} é maior que 0'
            case numero if numero < 0:
                return f'{numero} é menor que 0'
            case _ as numero:
                return f'{numero} é igual a 0'

b1 = AnalisaNumero(0)
print(b1.Analisa())