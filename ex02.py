vsegundos = int(input('Digite um valor em segundos: '))
vhoras = vsegundos // 3600
vminutos = vsegundos // 60 - (vhoras * 60)
vsfinal = vsegundos - (vsegundos // 60 * 60)
print(f'{vsegundos} segundos corresponde a {vhoras} horas, {vminutos} minutos e {vsfinal} segundos.')
