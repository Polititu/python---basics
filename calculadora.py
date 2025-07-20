''' calculadora de dois números com while ( adição, subratração, multiplicação e divisão)'''
r1 = input('Deseja abrir a calculadora? ([s]im ou [n]ão)')
if r1 == 's' :
  while True:
    n1 = input('Digite um número: ')
    n1 = float(n1)
    n2 = input('Digite outro número:')
    n2 = float(n2)
    op = input('Que operação deseja realizar entre esses números?' \
    ' Adição [A] Subtração [S] Multiplicação [M] Divisão [D]')
    op = op.capitalize()
    if op == 'A':
      print(n1 + n2 )
    elif op == 'S':
      print(n1 - n2)
    elif op == 'M':
      print (n1*n2)
    elif op == 'D':
      print(n1 / n2)
    else: 
      print('Desculpa, não entendi')
else: 
  print('Então tá bom')
print('=fim')