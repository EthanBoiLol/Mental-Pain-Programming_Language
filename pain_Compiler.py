# Pain Compiler V 1.00

# Created by Ethan

# MIT License


# The compiler convert the .pain file to .py file



import os
import importlib
#import tmp_pain
FileName = input("Input file name: ")

f = open(FileName, "r")

# values



## Start reading file line by line

lines = f.readlines()


def WriteTmp(write):
  t = open("tmp_pain.py", "a")
  t.write(write)
  t.close()


def ClearTmp():
  t = open("tmp_pain.py", "w")
  t.write("")
  t.close()


def Run(py):
  os.system("python3 " + py)


# Main Program


ClearTmp()

WriteTmp("from PVM import * \n \n")



i = 0
j = 0

# Replace pain stuff with python
while i < len(lines):
 lines[i] = lines[i].replace(";", "#")
 lines[i] = lines[i].replace('"', "")
 lines[i] = lines[i].replace("'", "")
 lines[i] = lines[i].replace("print", "")
 lines[i] = lines[i].replace("import ", "")
 lines[i] = lines[i].replace("FR IN * IMPIMP ", "import lib.")
 lines[i] = lines[i].replace("while", "")
 lines[i] = lines[i].replace("WHL", "while")

 if lines[i][0] == "i" and lines[i][1] == "f":
  lines[i] = lines[i].replace("if", " ")
 lines[i] = lines[i].replace("IF ", "if ")
 lines[i] = lines[i].replace("elif ", " ")
 lines[i] = lines[i].replace("orif ", "elif ")
 lines[i] = lines[i].replace("else ", " ")
 lines[i] = lines[i].replace("otherwise", "else")
 lines[i] = lines[i].replace("for ", "")
 lines[i] = lines[i].replace("FOR", "for")

 lines[i] = lines[i].replace(" and ", "")
 lines[i] = lines[i].replace("@", "and")
 lines[i] = lines[i].replace(" or ", "")
 lines[i] = lines[i].replace("$", "or")
 lines[i] = lines[i].replace("input", "")


 i += 1

i = 0


## Loops through each line

while i < len(lines):
  WriteTmp(lines[i])
  i += 1




Run("tmp_pain.py")
