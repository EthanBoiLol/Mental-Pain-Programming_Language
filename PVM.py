# Pain Virtual Machine V 1.00

# Created by Ethan

# MIT License

# The Virtual machine will run the converted py file to run special functions



import os


LET_STORE = [
    ' ',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
    '\n'
]

# Show command error, will just ignore
def ERR(text):
  print("PAIN ERROR: " + text)


# Prints stuff to screen
def PRI(Content):
  print(Content, end='')

# Get Character
def LET(num):
  return LET_STORE[num]

# Convert number to string
def NUM(num):
  return str(num)





# Adds value

def ADD(Val, val2):
  return Val + val2

# Subtract value

def SUB(Val, val2):
  return Val - val2

def INP(text):
  tmp = input(text)
  return int(tmp)

def INS(text):
  return input(text)
