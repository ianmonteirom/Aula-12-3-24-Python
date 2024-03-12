# encanador = R$80 por dia

num_dias = int(input('Número de dias trabalhados pelo encanador: '))
pagamento = 80 * num_dias
imposto = pagamento * 8 / 100
total = pagamento - imposto

print(f'Quantia líquida a ser paga: R${total}.')
