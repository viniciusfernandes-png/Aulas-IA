#Ana: 12345678
#Rodrigo: 656565656
#Incluir um número
#Listar os números todos
#Consultar o número de uma pessoa

def incluir(nome, tel, contatos):
    if nome in contatos:
      return False
    contatos[nome] = tel
    return True

def lista_todos(contatos):
    for contatos in contatos.items():
        print (f'{contato.key}: {contato.value}')

def consultar(nome, contatos):
    if nome in contatos:
        return
    else:
        return (f'{nome} não existe')
    
def menu():
    contatos = {}
    opcoes= '0-Sair\n1-Incluir\n2-Consultar\n3-Ver todos\n'
    op = int(input(opcoes))
    while(op !=0):
        if op == 1:
            nome = input("Digite o Nome")
            tel = input("Digite o Telefone")
        if incluir(nome, tel, contatos):
            print("Cadastro Ok")
        else:
            print("cadastro NOK")
        op = int(input(opcoes))

menu()
        


    



# notas = [7, 10, 10,  6, 4, 1, 0, 10]
# media = 0
# for nota in notas:
#     #media = media + nota
#     media += nota
# media = media / len(notas)
# print(f'Eis a média: {media}')


#while
#permitir que o usuário tente apenas 3 vezes 
#bloquear o acesso na terceira




#  senha = '123456'
# numero_tentativas = 1
# tentativa = input("Digite a senha\n")
# while senha != tentativa and numero_tentativas < 3:
#     print("Tente de novo")
#     tentativa = input ("Digite a senha\n")
#     numero_tentativas = numero_tentativas + 1
# if(numero_tentativas < 3):
#     print("Ok, acesso liberado\n")
# else:
#     print ("Acesso bloqueado")




# senha = '123456'
# tentativa = input("Digite a senha\n")
# while senha != tentativa:
#     print("Tente de novo")
#     tentativa = input ("Digite a senha")
# print("Ok, acesso liberado\n")



# def somar(a ,b):
#     return a + b

# def subtrair (a,b):
#     return a - b

# def multiplicar (a,b):
#     return a * b

# def dividir (a,b):
#     return a / b

# def elevar (a,b):
#     return a ** b

# def menu():
#     op =int (
#       input ("1-Somar\n2-subtrair\n3-multiplicar\n4-dividir\n5-elevar\n")
#     )
#     if op < 1 or op > 5:
#          print(f'A opção {op} é invalida')
#     else:
#         a =int( input ("Digite o primeiro operando"))
#         b = int( input ("Digite o segundo operando"))
#         if op == 1:
#             res = somar (a,b)
#             print(res)
#         elif op == 2:
#             res = subtrair (a,b)
#             print(res)
#         elif op == 3:
#             res = multiplicar (a,b)
#             print(res)
#         elif op == 4:
#             res = dividir (a,b)
#             print (res)
#         elif op == 5:
#             res = elevar (a,b)
#             print (res)

#         else:

   
# menu()





# # res1 = somar(2,3)
# # res2 = somar(5,6)

# # print (res1,res2)
