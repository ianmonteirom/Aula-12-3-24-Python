brancos = int(input('Total de votos brancos: '))
nulos = int(input('Total de votos nulos: '))
validos = int(input('Total de votos válidos: '))
total = brancos + nulos + validos
porcbrancos = brancos / total * 100
porcnulos = nulos / total * 100
porcvalidos = validos / total * 100

print(f'Total de votos: {total}. \n'
      f'Porcentagem de votos Brancos: {porcbrancos:.1f}% \n'
      f'Porcentagem de votos Nulos: {porcnulos:.1f}% \n'
      f'Porcentagem de votos Válidos: {porcvalidos:.1f}%')
