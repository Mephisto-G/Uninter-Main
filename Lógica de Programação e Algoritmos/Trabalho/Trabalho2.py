print('(=^･ω･^=) Bem vindo, a loja de marmitex do *Gabriel Alves Oliveira* (=^･ω･^=))')
print('Essas são as opções disponiveis')
print(' ')
print('P - (BA)Bife Acebolado R$16 \n    (FF) Filé de Frango R$15')
print(' ')
print('M - (BA)Bife Acebolado R$18 \n    (FF) Filé de Frango R$17')
print(' ')
print('G - (BA)Bife Acebolado R$22 \n    (FF) Filé de Frango R$21')
print(' ')

acumulador = 0
bap = 16
ffp = 15
bam = 18
ffm = 17
bag = 22
ffg = 21

#Programa principal
while True: #Continuara executando até que digite sair
    
    sabor = input('Deseja BA ou FF? ')
    if  sabor.upper() not in ('BA', 'FF'): #sabor errado
        print('Sabor inválido. Tente novamente')
        continue

    tamanho = input('Qual tamanho deseja? ')
    if  tamanho.upper() not in ('P','M','G'):#Tamanho errado
        print('Tamanho errado. Tente novamente')
        continue

    elif sabor.upper() == 'BA' and tamanho.upper() == 'P':
         print(f'Você pediu Bife Acebolado no tamanho {tamanho}: R${bap}') #saida com o pedido selecionado
         acumulador += bap
    elif sabor.upper() == 'FF' and tamanho.upper() == 'P':
         print(f'Você pediu Filé de Frango no tamanho {tamanho}: R${ffp}')
         acumulador += ffp

    elif sabor.upper() == 'BA' and tamanho.upper() == 'M':
         print(f'Você pediu Bife Acebolado no tamanho {tamanho}: R${bam}')
         acumulador += bam
    elif sabor.upper() == 'FF' and tamanho.upper() == 'M':
         print(f'Você pediu Filé de Frango no tamanho {tamanho}: R${ffm}')
         acumulador += ffm
    
    elif sabor.upper() == 'BA' and tamanho.upper() == 'G':
         print(f'Você pediu Bife Acebolado no tamanho {tamanho}: R${bag}')
         acumulador += bag 
    elif sabor.upper() == 'FF' and tamanho.upper() == 'G':
         print(f'Você pediu Filé de Frango no tamanho {tamanho}: R${ffg}')
         acumulador += ffg

    escolha = input('Deseja pedir mais alguma coisa?')

    if escolha.upper() == 'SIM': #Recomeça o loop
        continue
    else: #Termina o loop
        break
print(f'O valor total do pedido é: R${acumulador}')
print('Obrigado por comprar na minha loja ＼(＾O＾)／')


    
    
    


    