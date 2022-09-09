# 4. Crie  um  programa  em  linguagem  Python  que  recebe  do  usuário  um  valor  de  temperatura  em  graus Celsius e o converta para Fahrenheit ou Kelvin. O usuário deve informar “F” ou “f” caso queira efetuar a conversão para Fahrenheit e “K” ou “k” caso desejeconverter o valor de temperatura para Kelvin. Caso  qualquer  outra  letra  seja  informada,  deve  ser  exibida  a  mensagem  “Opção  inválida  de conversão!”.A  seguir  são  apresentadas  as  equações  para  converter  um  valor  de  temperatura  de Celsius (𝐶) para Fahrenheit (𝐹) e Kelvin (𝐾), respectivamente

# f = 9/5.c + 32 
# k = c + 273 . 155

from pickletools import string1


def ConversorTemperaturas(celsius : float, op : str) -> str:
    match op.lower():
        case operation if operation == 'k':
            return f'\nKevin = {((9/5) * celsius) + 32}'
        case operation if operation == 'f':
            return f'\nFarenheit = {celsius + (273 * 155)}'
        case _:
            return '\nOpção inválida de conversão'

print('Conversor de Temperaturas')

while True:

    print(ConversorTemperaturas(float(input('\nInforme a temperatura em celsius: ')), input('Informe a operação de conversão [f/k]: ')))

    loop = input('\nQuer informar mais algum número[S/N]: ')

    match loop.upper():
        case info if info == 'S':
            continue
        case info if info == 'N':
            break
        case _:
            print('Opção Inválida')
            break
