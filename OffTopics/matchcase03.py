# 3. Considere que uma determinada lista de contatostelefônicos  encontre-se possua os registrosapresentados na tabela a seguir. Desenvolva um programa em Python que permite que o usuário digite o nome de um  contato que pretende consultar e, em seguida,exibeem tela o número  telefônico correspondente. Caso o contato não exista na lista, deve ser exibida a mensagem: “Contato não encontrado".

# Conhecimentos Utilizados;
# - Funções
# - Dicionários(Hashs)
# - Operadores Lógicos
# - Estrutura de repetição While
# - Pattern Matching
# - POO


# Paradigma Estrutural
def verificacontato(agenda = {'Maria' : '9111-1111', 'Joana' : '92222-2222', 'Joaquim' : '93333-3333', 'Pedro' : '94444-4444'}):
    match agenda.keys():
        case nome if input('Informe o nome do contato: ') in nome:
            return f'Este nome está salvo na sua lista de contatos'
        case _:
            return f'Este nome não está salvo na sua lista de contatos'

while True:
    print(verificacontato())
    
    operation = input('Quer ver outro contato [S/N]?')
    
    match operation.upper():
        case oracao if oracao == 'S':
            continue
        case oracao if oracao == 'N':
            break
        case _:
            print('Opção inválida')
            break
