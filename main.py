from simulateDfa import simulateDfa
from program import program
import sys

class Dfa:
    def __init__(self):
        file_name = input('Digite o nome do arquivo do autômato: ')
        with open(file_name) as dfa_file:
            dfa_data = dfa_file.read()

        dfa = eval(dfa_data)
        self.dfa = dfa

    def run(self):
        program(self.dfa)

if __name__ == "__main__":  
    dfa1 = Dfa()
    dfa1.run()