def simularDfa(dfa, input):
    state = dfa['initial_state']
    acept = False
    counter = 0
    while counter < len(input):
        c = input[counter]
        if c not in dfa['sigma']:
            print(f'O símbolo {c} não pertence ao alfabeto do autômato!')
            break
       
        if state not in dfa['states']:
            print(f'O estado {state} não pertence ao conjunto de estados do autômato!')
            break

        try:
            print(f'o c agora é: {c}')
            print(f'o estadoanterior é: {state}')
            state = dfa['delta'][(state, c)]
            print(f'estado atual: {state}')
        except:
            print(f'Não foi possível realizar a transição do estado {state} com entrada {c}')
            break

        counter += 1
    
    if state in dfa['final_states'] and counter == len(input):
        acept = True
        
    if acept:
        print(f'A cadeia {input} foi aceita pelo autômato!')
    else:
        print(f'A cadeia {input} foi rejeitada pelo autômato!')