numero = float(input('Digite um número: '))

match numero:
    case numero if numero > 0:
        print('Positivo')
    case numero if numero < 0:
        print('Negativo')
    case _:
        print('Neutro')