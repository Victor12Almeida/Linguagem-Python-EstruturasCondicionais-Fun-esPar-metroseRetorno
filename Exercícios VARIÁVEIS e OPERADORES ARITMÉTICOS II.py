'''1) Na sua lista de compras do mercado, constam apenas 3 itens: arroz, batata palha e um suco de garrafa. Porém, você possui apenas uma nota de R$100 para pagar. Faça um programa no qual sejam digitados os valores dos itens e mostre na tela valor que você deve receber (troco).'''

# arroz = float(input('Digite o valor do arroz: '))
# batata_palha = float(input('Digite o valor da batata palha: '))
# suco = float(input('Digite o valor do suco : '))

# total = arroz + batata_palha + suco
# troco = 100 - total
# print ('Seu troco é: ', troco)



'''2) Na volta as aulas cada aluno(a) ganhará 2 bombons (1 para si e 1 para os pais), além de 1 bombom para o(a) professor(a). Faça um programa no qual seja digitado a quantidade de alunos da turma e mostrando quantos bombons no total devem ser comprados.'''

# alunos = int(input('Digite a quantidade de alunos? '))

# professor = 1

# print(f'Deverá ser comprados: {alunos*2+professor} bombons.')


'''3) Um(a) programador(a) deseja, ao final do mês, saber quantas horas por semana em média estudou programação. Crie um programa no qual seja digitado a quantidade de horas de cada semana do mês e no final mostre a média de horas por semana naquele mês.'''

# horas_estudadas = float(input('Digite as horas estudadas na primera semana: '))
# horas_estudadas2 = float(input('Digite as horas estudadas na segunda semana: '))
# horas_estudadas3 = float(input('Digite as horas estudadas na terceira semana: '))
# horas_estudadas4 = float(input('Digite as horas estudadas na quarta semana: '))

# total_estudado = int(horas_estudadas + horas_estudadas2 + horas_estudadas3 + horas_estudadas4)

# media_estudada = total_estudado / 4

# print(f'A média estudada por semana foi de: {media_estudada} horas por semana.')


'''4) Uma feira de livros está fazendo promoção onde na compra de 3 livros, o(a) comprador(a) ganha 15% de desconto. Criar um programa que receba os valores dos 3 livros e mostra na tela o total dos livros sem desconto e com desconto.'''

# valor_livro1 = float(input('Digite o valor do primeiro livro: '))
# valor_livro2 = float(input('Digite o valor do segundo livro: '))
# valor_livro3 = float(input('Digite o valor do terceiro livro: '))

# valor_total = valor_livro1 + valor_livro2 + valor_livro3
# valor_ComDesconto = valor_total - (valor_total * ( 15 / 100 ))

# print(f'O valor total do seu pedido é: R${valor_total}\nCom o desconto de 15% o valor fica por:R${valor_ComDesconto} ')


'''5) Você é um amante da natureza e adora fazer trilhas. Criar um programa que calcule a velocidade média das trilhas que você realiza. Para isso, devem ser digitados os dados de distância percorrida (quilômetros) e tempo que a trilha durou (horas). Fazer então o cálculo da velocidade média e mostrar na tela a mensagem "Sua média de velocidade durante essa trilha foi de X km/h", sendo X a velocidade. '''

'''6) Crie um programa no qual o usuário deve digitar um número (base) e o seu expoente. Apresentar na tela o resultado da exponenciação.'''

# numero = float(input('Digite um número base: '))
# exponente = float(input('Digite exponente: '))
# print('O expoente do número digitado é:',numero**exponente)

'''7) Os leões baios são animais territoriais. Seu território compreende cerca de 320km² por indivíduo, exceto quando formam casais, nesse caso o casal costuma dominar uma área de 400km², juntos. Considerando que existam 9 fêmeas e 5 machos em determinada reserva ambiental. Elaborar um programa no qual você deve digitar quantos casais (dados de pesquisa de campo) existem dentre esse total e mostrar na tela a soma geral de área dominada, incluindo todos indivíduos.'''

'''8) Criar um programa que realize o cálculo de uma média da faculdade. A média é composta por três notas: Atividade Individual (peso 1), Seminário em Equipe (peso 1), Projeto final (peso 3). O usuário deve digitar as três notas e a média deve ser mostrada na tela.'''

# nota1 = float(input('Digite a nota da Atividae Individual: '))
# nota2 = float(input('Digite a nota da Seminário em Equipe: '))
# nota3 = float(input('Digite a nota da Projeto final: '))

# nota_media = (nota1 + nota2 + nota3) / 3

# print('A sua média é:',nota_media)

'''9) Seu sonho é construir uma piscina. Para cada metro quadrado, são necessários 120 azulejos. O cálculo de área em metros quadrados, é feito multiplicando a largura pelo comprimento. Digitar os valores (em metros) da largura e comprimento que deseja a piscina. Mostrar na tela a quantidade de azulejos que devem ser comprados e o valor total a ser pago, sendo que uma caixa de azulejo com 60 unidades custa R$45,50.'''

'''10) Desenvolver um programa que realize o cálculo de consumo de combustível por quilometragem, para veículos (km por litro). Para isso, devem ser digitados os dados de distância total percorrida (km) e total de combustível gasto (litros), mostrando o resultado ao final.'''

# distancia = float(input('Digite a distância percorrida: '))
# gasolina = float(input('Digite o total de gasolina consumida: '))

# combustivel_km = distancia / gasolina

# print(f'O consumo do carro é de: {combustivel_km} km/l.')

'''11) Um festival de música está terceirizando a montagem da estrutura. A empresa contratada necessita saber uma estimativa de público para calcular a quantidade de bares e banheiros. O cálculo utilizado é de 1 banheiro para cada 50 pessoas e 1 bar para cada 150 pessoas. Criar um programa onde seja digitado o público esperado e mostrar na tela em média quantos banheiros e bares seriam necessários.'''

# publico = float(input('Digite o total de público esperado: '))
# banheiro = publico / 50
# bar = publico / 150

# print(f'A média de banheiros/bar necessária para esse evento será de: {banheiro:.0f} banheiros e {bar:.0f} bares.')

'''12) Uma pousada cobra R$280 reais a diária por quarto e R$15 reais o café por pessoa por dia. Você pretende passar um tempo com alguns amigos nessa pousada, sendo que todos ficarão no mesmo quarto. Informar a quantidade de pessoas, o número de diárias e quantas pessoas do grupo vão querer café diário. Mostrar na tela o total a pagar.'''

# pessoas = int(input('Quantas pessoas? '))
# qts_diarias = int(input('Quantas diárias? '))
# cafe = int(input('Quantas pessoas irão tomar café? '))

# diarias_custo = 280 * qts_diarias
# cafe_custo = 15 * cafe
# custo_total = diarias_custo + cafe_custo

# print(f'O toltal será de: {custo_total}')

'''13) Um festival de balonismo oferece passeios de balão. Para cada 5 minutos de voo, são necessários 10m³ (metros cúbicos) de gás, sendo que o metro cúbico de gás custa R$15 reais. No balão cabem no máximo 4 pessoas. O cálculo do valor do passeio é feito somando o valor gasto em gás, mais uma taxa de R$20 reais por pessoa. Criar um programa que pergunte quantas pessoas vão no passeio e o tempo de passeio. Mostrar na tela o total cobrado pelo passeio.'''

# qts_pessoas = int(input('Digite o números de pessoas: '))
# tempo_passeio = float(input('Digite o tempo do passeio(em minutos): '))

# qtd_passeio = (tempo_passeio / 5)* 10
# custo_passeio = qts_pessoas * 15
# custo_total = custo_passeio + (qts_pessoas * 20)
# print('O valor do Passeio custará: R$',custo_total)





'''14) As baleias da Groênlandia estão entre os animais que vivem mais tempo na Terra, em média 200 anos. A reprodução se dá a cada 4 anos, tendo somente 1 filhote por vez. Programar um sistema que calcule o total de filhotes ao longo da vida e a média de filhotes de uma baleia dessa espécie por década.'''

# baleia = 