lista = []
dec0 = input('Deseja abrir sua lista de compras: [s]im ou [n]ão ')
indices = range(len(lista))
if dec0 == 's':
  if dec0 == 's':  
    while dec0 == 's':
        indices = range(len(lista))
        dec1 = input ('O que deseja fazer na sua lista: \n [i]nserir [a]pagar [l]istar')
        if dec1 == 'i' :
          dec2 = input('Escreva o que deseja inserir:')
          lista.append(dec2)
          print('item adicionado')
          print('A lista está assim')
          for item in enumerate(lista):
            indice, nome = item
            print(indice, nome)
        if dec1 == 'a':
          dec3 = input('Deseja apagar por [i]ndice ou por [n]ome')
          if dec3 == 'i':
            while True:
              dec4 = int(input('Digite o indice:'))
              if dec4 not in indices:
                print('esse indice não está na lista')
                continue
              else:
                lista.pop(dec4)
                print('item execluido')
                print('A lista está assim')
                for item in enumerate(lista):
                  indice, nome = item
                  print(indice, nome)
                break
          if dec3 == 'n':
            while True:
              dec5 = input('Digite o nome que deseja buscar:')
              if dec5 not in lista:
                print('o nome não está na lista')
                continue
              else:
                lista.remove(dec5)
                print('objeto removido')
                print('A lista está assim')
                for item in enumerate(lista):
                  indice, nome = item
                  print(indice, nome)
                break
        if dec1 == 'l':
          print(lista)
        dec0 =input('Ainda deseja mexer na sua lista? [s]im ou [d]epois')
        indices = range(len(lista))
  if dec0 == 'd':
    print('Ok. Então aqui está sua lista')
    for item in enumerate(lista):
      indice, nome = item
      print(indice, nome)
  else:
    print('digite s ou d ')
if dec0 == 'n':
  print('tudo bem')
else: 
  print('digite s ou n ')
