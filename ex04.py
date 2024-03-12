vreal = float(input('Digite um valor em reais: R$'))
cotdolar = float(input('Digite a cotação do dólar: R$'))
vdolar = vreal / cotdolar
print(f'R${vreal} convertido em dólares valem R${vdolar:.2f}.')
