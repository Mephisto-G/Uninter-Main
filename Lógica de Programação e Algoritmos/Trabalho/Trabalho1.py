print('Bem vindo, Gabriel Alves Oliveira')
valorDoPedido = float(input('Qual é o valor do pedido? '))
quantidadeParcelas = int(input('Qual é a quantidade de parcelas? '))

#Programa principal
if quantidadeParcelas < 4: #Verifica se o valor do pedido atende o requisito
    valor = valorDoPedido *(1 + 0) #Faz o calculo do juros
    valor2 = int(valor/ quantidadeParcelas) #Pega o valor apos passar pelo tratamento de juros e divide pelas parcelas
    print(f'O valor das parcelas é de: R${valor2}')
    print(f'O valor final sera de: R${valor}')


elif quantidadeParcelas >= 4 and quantidadeParcelas < 6: 
     valor = valorDoPedido * (1 + 0.04)
     valor2 = int(valor/ quantidadeParcelas)
     print(f'O valor das parcelas é de: R${valor2}')
     print(f'O valor final sera de: R${valor}')

elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
     valor = valorDoPedido * (1 + 0.08)
     valor2 = int(valor/ quantidadeParcelas)
     print(f'O valor das parcelas é de: R${valor2}')
     print(f'O valor final é: R${valor}')

elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
     valor = valorDoPedido * (1 + 0.16)
     valor2 = int(valor/ quantidadeParcelas)
     print(f'O valor das parcelas é de: {valor2}')
     print(f'O valor final sera de: {valor}')

else:
     valor = valorDoPedido * (1 + 0.32)
     valor2 = int(valor/ quantidadeParcelas)
     print(f'O valor das parcelas é de: R${valor2}')
     print(f'O valor final sera de: R${valor}')
