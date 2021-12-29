print('Bem-vindo(a) ao verificador de números primos!!!\n')
number = input('Digite o número que deseja verificar:')

while not number.isnumeric():
    print('\nVocê não digitou um número válido, tente novamente.\n')
    number = input('Digite o número que deseja verificar:')

number = int(number)

if number == 2:
    print(f'O número {number} é primo.')

rest = 0
for i in range(2, number):
    rest = number % i

    if rest == 0:
        print(f'O número {number} não é primo.')
        break

if rest != 0:
    print(f'O número {number} é primo.')
