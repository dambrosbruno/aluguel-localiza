#ALUGUEL LOCALIZA
day1 = int(input('Quantos dias você utilizará o carro: '))
day2 = float(input('Preço da diária do carro: '))
day3 = day1 * day2
print('O total de aluguel do carro será de R$ {:.2f}'.format(day3))

gas1 = float(input('Preço do litro de alcool: '))
gas2 = float(input('Capacidade do tanque em litros: '))
gas3 = float(input('Litros gastos do tanque: '))
gas4 = gas2 - gas3
print('Litros restantes para completar o tanque: {:.2f}'.format(gas4))
gas5 = gas3 * gas1
print('Preço do tanque restante será de R$ {:.2f}'.format(gas5))

total = day3 + gas5
print('O valor total da viagem será de R$ {:.2f}'.format(total))