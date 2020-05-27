from main import type_out, type_out_input
from player import Player
from time import sleep

def beginning(Player):
    type_out('\nYour story begins in highschool...\n')
    sleep(.5)
    type_out('I know... everyone hates high school, but don\'t worry, since this story begins with the end of highschool...')
    sleep(.5)
    type_out('\nThat\'s right... you just graduated from highschool!!')
    sleep(.5)
    type_out('\n\nCongratulations!!!!\n')
    sleep(.5)
    type_out('\nHowever, this also comes with a caveat...')
    type_out('\nYou always told everyone that you would wait until the end of highschool to figure out what you wanted to do with your life, but now you\'re here and you have no idea what to do...')
    type_out('\nSo...... now it\'s time to choose...')
    type_out('\nWhat do you want to do with your life?\n')
    sleep(.5)
    type_out('\nSorry, that\'s a hard question.. \nLet me make it easier for you.\nI\'ll give you a few options, and you can decide which one you want to take.')
    answer = type_out_input('\nIs that Okay? (y/n)\n')
    if (answer=='y'):
        choose_path(player)
    else:
        type_out('\nI don\'t think you understand... you\'re supposed to type \'y\'... Please try again..')
        answer = type_out_input('\nIs that Okay? (y/n)\n')
        if (answer!='y'):
            answer = type_out_input('\nDude... come on.. just type y\n')
            if (answer!='y'):
                answer = type_out_input('\nLast chance or I\'m giving up on you...\nJust type out \'y\'\n')
                if (answer!='y'): type_out('\nI gave you a chance... sorry')



player = Player()
beginning(player)
