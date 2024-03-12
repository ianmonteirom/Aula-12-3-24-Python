comp = float(input('Digite o comprimento da cozinha: '))
larg = float(input('Digite a largura da cozinha: '))
alt = float(input('Digite a altura da cozinha: '))

area = (larg * alt) * comp
print(f'Total de caixas de azulejos necessários: {area / 1.5:.2f}')

