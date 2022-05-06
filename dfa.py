with open('m.dfa') as dfa_file:
    dfa_data = dfa_file.read()

dfa = eval(dfa_data)

print(dfa['delta'])