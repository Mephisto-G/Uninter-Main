print('Bem vindo a Fábrica de Camisetas do Gabriel Alves Oliveira \n \n')
print('*Entre com o modelo desejado*')
print('MCS - Manga Curta Simples\nMLS - Manga Longa Simples\nMCE - Manga Curta Com Estampa\nMLE - Manga Longa Com Estampa')
mcs = 1.80
mls = 2.10
mce = 2.90
mle = 3.20
numero = 0

def escolha_modelo():#Escolhe o modelo da camiseta
  while True:
    modelo = input(' ')
    if modelo.lower() == 'mcs':
        print(f'O valor desse modelo é R$:{mcs}')
        return mcs

    elif modelo.lower() == 'mls':
        print(f'O valor desse modelo é R$:{mls}')
        return mls

    elif modelo.lower() == 'mce':
        print(f'O valor desse modelo é R$:{mce}')
        return mce

    elif modelo.lower() == 'mle':
        print(f'O valor desse modelo é R$:{mle}')
        return mle

    else:
      print('Modelo inexistente, tente novamente')
      continue

def num_camisetas(x):#Calcula o valor da camiseta*quantidade subtraindo o desconto
  try:
    while True:
      global numero
      numero = int(input('Quantas camisetas deseja? '))
      
      if numero < 20:
         valor = numero * escolha
         return valor
       
      
      elif 20 <= numero < 200:
        valor = (numero * escolha) * 0.95
        return valor

      elif 200 <= numero < 2000:
        valor = (numero * escolha) * 0.93
        return valor

      elif 2000 <= numero < 20000:
         return (numero * escolha) * 0.88

      else:
        print('Não aceitamos nessa quantidade')
        continue

  except ValueError:
    print('Não é um numero, tente novamente')
    num_camisetas(x)

def frete(): #Calcula o valor do frete
  while True:
    print('*Frete*')
    print('1 Transportadora R$100\n2 Sedex R$200\n3 Retirar na fabrica R$0')
    preco = int(input(' '))

    if preco == 1:
       return 100
    
    elif preco == 2:
       return 200
    
    elif preco == 0:
       return 0
    
escolha = escolha_modelo()
valor1 = (num_camisetas(escolha))
valor2 = frete()
print(f'Total do pedido é de R$',valor1 + valor2,' (modelo:', escolha, '* Quantidade(com desconto): R$',(numero * escolha)-valor1,'+ frete: R$',valor2) #Encerra o programa informando o valor da compra