import sys
from time import sleep

def type_out(sentence):
    for char in sentence:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

def type_out_input(question):
    for char in question:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    return input('')
