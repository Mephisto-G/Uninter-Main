lista_funcionarios=[]
id_global=5217667
def cadastrar_funcionario(x):# Realiza o cadastro
  try:
        nome=input('Nome do funcionario: ').upper()
        setor=input('Setor do funcionario: ').upper()
        salario=int(input('Salario do funcionario:'))
        lista_funcionarios={'id' :x,'nome':nome, 'setor':setor,'salario':salario }
        return lista_funcionarios
  except ValueError:
      print('Algo deu errado, tente novamente')
      cadastrar_funcionario()
      
def consultar_funcionarios(x):#Faz a consulta de usuarios cadastrados
    try:    
        while True:
            print('1 Consultar Todos\n2 Consultar por id\n3 Consultar por Setor\n4 Retornar ao menu')
            escolha = int(input(' '))
            if escolha == 1:
                for i in x:
                    for chave, valor in i.items():
                        print(f'{chave}: {valor}','\n')

            elif escolha == 2:
                while True:
                    funcionario_id = int(input('Forneça o ID: '))
                    if funcionario_id == '':
                        break
                    for i in x:
                        if i['id'] == funcionario_id:
                            for chave, valor in i.items():
                                print(f'{chave}: {valor}\n')

                        else:   
                             print(f'Id: {funcionario_id} não encontrado!')
                             continue
    
            elif escolha == 3:
                while True:
                    funcionario_setor = input('Informe o setor: ').upper()
                    if funcionario_setor == '':
                        break
                    for i in x:
                        if i['setor'] == funcionario_setor:
                            for key, value in i.items():
                                print(f'{key}: {value}\n')
                   
                        else:
                            print(f'setor {funcionario_setor} não encontrado')
                            continue
  
            elif escolha == 4:
                 return
            
            elif escolha not in (1,2,3,4):
                print('Opção Invalida, tente novamente')
                continue

    except:
        print('Algo deu errado, tente novamente')
        consultar_funcionarios(x)

def remover_funcionario(x):#remove os usuarios
    try:
        while True:
            for i in x:
                tirar_funcionario=int(input('Forneça o id: '))
                if i['id'] == tirar_funcionario:
                    x.remove(i)
                    print(f'O id:{tirar_funcionario} foi removido com sucesso!')
                    
                else:
                    print(f'o id:{tirar_funcionario} não foi encontrado')
                    continue

    except ValueError:
        print('Algo deu errado, tente novamente')
#Programa principal
while True:
    print('\nBem vindo a empresa de Gabriel Alves Oliveira')
    print('-' *len('Bem vindo a empresa de Gabriel Alves Oliveira'))
    print('-'*15,'Menu Principal','-'*15,'\n')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Funcionários\n2 - Consultar Funcionários(s)\n3 - Remover Funcionário\n4 - Sair')
    escolha=int(input(' '))
    id_global +=1
    if escolha == 1:
        lista_funcionarios.append(cadastrar_funcionario(id_global))
        continue

    elif escolha == 2:
        consultar_funcionarios(lista_funcionarios)
        continue
    
    elif escolha == 3:
        remover_funcionario(lista_funcionarios)
        continue
    
    elif escolha == 4:
        break

print('Encerrando o programa....')











