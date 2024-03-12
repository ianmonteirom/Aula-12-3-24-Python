# custo = custofabrica + porcentagemdistribuidor (28%) + impostos (45%)

custo_fabr = float(input('Digite o valor do custo de fábrica do carro novo: R$'))
porc_distr = custo_fabr * 28 / 100
impostos = custo_fabr * 45 / 100
custo_final = custo_fabr + porc_distr + impostos

print(f'O custo final deste carro novo será de R${custo_final}.')
