# cada paozin = R$0,38
# cada broa = R$4,50

total_paes = int(input('Total de pães vendidos no dia: '))
total_broas = int(input('Total de broas vendidas no dia: '))

vpaes = total_paes * 0.38
vbroas = total_broas * 4.50
valor_total = vpaes + vbroas

print(f'Total arrecadado com a venda de pães e broas no dia: R${valor_total:.2f}.')

porc_poup = valor_total * 10 / 100

print(f'Valor para a poupança (10% do valor total): R${porc_poup:.2f}.')
