a = int(input('Primeiro Bimestre: '))
if a > 10 :
  a = int(input('Você digitou um valor errado, permitimos somente valores de 0 a 10. Por favor, Digite a média do Primeiro Bimestre novamente: '))
b = int(input('Segundo Bimestre: '))
if b > 10 :
  a = int(input('Você digitou um valor errado, permitimos somente valores de 0 a 10. Por favor, Digite a média do Segundo Bimestre novamente: '))
c = int(input('Terceiro Bimestre: '))
if c > 10 :
  a = int(input('Você digitou um valor errado, permitimos somente valores de 0 a 10. Por favor, Digite a média do Terceiro Bimestre novamente: '))
d = int(input('Quarto Bimestre: '))
if d > 10 :
  a = int(input('Você digitou um valor errado, permitimos somente valores de 0 a 10. Por favor, Digite a média do Quarto Bimestre novamente: '))
  
mediaAnual=(a+b+c+d) / 4
print('Sua media anual é: {}'.format(mediaAnual))
