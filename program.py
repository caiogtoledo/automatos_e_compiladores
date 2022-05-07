from simulateDfa import simulateDfa
def program(dfa):
    while True:
        input_user = input("Digite a cadeia: ")
        print(input_user)
        if input_user.lower() == 'sair' or input_user == '':
            print('Programa finalizado pelo usuário!')
            break
        else:
            simulateDfa(dfa, input_user)
        print("-"*40)
        print("Digite 'sair' ou clique na tecla Enter ")
        print('para fechar o programa.')
        print("-"*40)