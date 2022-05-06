from simularDfa import simularDfa
import sys

class Dfa:
    def __init__(self):
        # self.fileName = fileName
        with open('m.dfa') as dfa_file:
            dfa_data = dfa_file.read()

        dfa = eval(dfa_data)
        self.dfa = dfa

    def run(self):
        simularDfa(self.dfa, '1110')


if __name__ == "__main__":  
    dfa1 = Dfa()
    dfa1.run()