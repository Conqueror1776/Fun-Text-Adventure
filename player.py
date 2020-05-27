import main
class Player:
    def __init__(self):
        self.name = main.type_out_input('Welcome. Before you begin your adventure, what is your name? \n \n')
        main.type_out('\nWelcome %s, your adventure is about to begin... \n' % self.name)
