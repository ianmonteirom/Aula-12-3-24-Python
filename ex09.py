total = 780000
ganhador1 = total * 46 / 100
ganhador2 = total * 32 / 100
ganhador3 = total - ganhador1 - ganhador2

print(f'A importância de R${total} será dividida em: \n'
      f'GANHADOR 1 = R${ganhador1:.2f}\n'
      f'GANHADOR 2 = R${ganhador2:.2f}\n'
      f'GANHADOR 3 = R${ganhador3:.2f}')
