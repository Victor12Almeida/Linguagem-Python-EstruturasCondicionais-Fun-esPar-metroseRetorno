'''1) Crie um algoritmo no qual seja digitado a distância percorrida em quilômetros, o tipo do carro e informe ao final a média de consumo estimado de combustível. Sabendo-se que um carro do tipo A faz 8km/litro, o carro do tipo B faz 12km/litro e o tipo C faz 9km/litro. Caso seja fornecido um tipo de carro inválido (diferente de A, B ou C) o algoritmo deve mostrar uma mensagem "Tipo de carro inválido!" e encerrar.'''

distancia = float(input('Digite a distância(km): '))
carro = input('Digite o carro (A/B/C): ')
carro_A = distancia / 8
carro_B = distancia / 12
carro_C = distancia / 9

if carro == 'A':
    print(f'Total do consumo de combustível é {carro_A:.2f} litros')
elif carro == 'B':
    print(f'Total do consumo de combustível é {carro_B:.2f} litros')
elif carro == 'C':
    print(f'Total do consumo de combustível é {carro_C:.2f} litros')
else:
    print('Tipo de carro inválido!')

