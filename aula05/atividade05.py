print('''
[1 a 9] - Positivo
[-1 a -9] - Negativo
[0] - Zero
''')

numero = float(input('Digite um número: '))

match numero:
    case numero if 1 <= numero <= 9:
        print('Positivo')
    case numero if -1 <= numero <= -9:
        print('Negativo')
    case 0:
        print('Zero')