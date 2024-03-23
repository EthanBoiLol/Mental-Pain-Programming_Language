# Mental Pain Programming Language (MPPL)

An esoteric programming language created in python that is created with the intention of causing you mental pain

## Requires

- python3
- os library
- importlib library
- bandaid (for mental pain)


## Getting started
How to start writing in Pain

1. create a file, it's recommended to end the file with **.pain**
2. write the Pain code in said file
3. to run the code, type `python main.py` or `python3 main.py`
4. when it ask you for a file, input your Pain code filename (include **.pain** if needed)
5. enjoy :)



## Documents


### Syntax

The syntax is very similar to that of *python*, however there are differences when writing in Pain

`;` - create comments

`FOR` - create a for loop

`=` - Create value

`WHL` - Create a while loop

`IF` - Create's an if statement

`orif` - Create's an "else if" statement

`otherwise` - create's an "else" statment

`@` - the equivalent of "and" within the if statement

`$` - the quivalent of "or" within the if statement

`FR IN * IMPIMP [library name]` - import's an external library

### Functions

in order to do 'tasks' in Pain, you must use functions. The following are the list of all default functions built-in to the runtime

`PRI(A)` - prints out the contents of 'A'

`ERR(description)` - prints any error messages

`LET(index)` - returns a character, *0* is space, *1-26* are the letters in order, and *27* is a new line

`NUM(number)` - Converts a number to a string, useful for the **PRI** function

`ADD(Variable, number to add)` - takes the first variable and adds the second to it, then returns the newly added number

`SUB(Variable, number to subtract)` - takes the first variable and subtracts the second to it, then returns the newly subtracted number

`INP(text to display)` - returns the user's integer input and stores it

`INS(text to display)` - returns the user's string input and stores it

### Other Factors
While programming in Pain, there are other factors to keep in mind

- This programming language does *not* accept quotation marks (") within the code, as the compiler will simply ignore them, to store any characters, please use a default function (such as *LET* or *IMS*)

- some default python functions do **NOT** work in Pain, such as `print()`. Please use the Pain's counterpart instead

- Pain doesn't import global libraries like other languages does, all libraries must be local and be located in a folder in the root directory called `/lib`

- Every project must have a copy of the compiler and virtual machine in order for the program to work correctly. Also, runtime and compiler must be at root directory


## Examples

### Hello World! Program

```
PRI(LET(8)) ; h
PRI(LET(5)) ; e
PRI(LET(12)) ; l
PRI(LET(12)) ; l
PRI(LET(15)) ; o

PRI(LET(27)) ; New Space

PRI(LET(23)) ; w
PRI(LET(15)) ; o
PRI(LET(18)) ; r
PRI(LET(12)) ; l
PRI(LET(4)) ; d

PRI(LET(27)) ; New Space

; Output:

; HELLO
; WORLD
```


### All syntax and functions program

```
; FR IN * IMPIMP testLib ; Commented to avoid error, but just to show how to do it


; This just does random things lol

VarA = 5

VarB = 7

VarC = 28

VarD = LET(1) + LET(2)

PRI(12)

PRI(VarD)

PRI(LET(1) + LET(3))

PRI(LET(7) + NUM(15))

j = 10

IF j > 2:
  SUB(j, 1)

orif j < 10:
  sub(j, 2)

otherwise:
  sub(j, 3)


o = 3

Arr = [5, 6, 7, 8]

FOR x in Arr:
  Arr = ADD(o, x)

PRI(o)

v = 150

WHL v > 0:
  v = SUB(v, 1)
  PRI(v)
  IF v > 50 @ v != 100:
    v = SUB(v, 5)

  orif v < 50 $ v == 78:
    v = SUB(v, 3)

PRI(v)

PRI(LET(27))

ERR(LET(8) + LET(9) + LET(27))

q = INP(LET(9) + LET(14) + LET(20) + LET(0))

w = INS(LET(20) + LET(24) + LET(20) + LET(0))

PRI(LET(27))

PRI(q)
PRI(w)
```

## License
This software was created by Ethan Seren and is licensed under the MIT license
```
MIT License

Copyright (c) 2024 Ethan Seren

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
