# SecretSanta
Small python project that facilitates the assignment of gifting in secret santa

Author: Ryan Hammarskjold

files: SecretSanta.py, RandomSanta.py, testing.py

dependencies: sys, os, random, numpy

python version: 2.7.12

SecretSanta.py requires two command line arguments: the name of the file in which 
it can find the names of all participants and a string that specifies the name of
the directory to which it will write all text files. The program then uses the
random library to schuffle names such that each person is assigned another person
that is not themself. Finally the gifting assignments are written to files named 
for the gifter that is in the given directory. 

Example Usage:

>more names.txt
A
B
C

>python SecretSanta.py names.txt test

>ls ./test
A.text   B.txt   C.txt

>more test/A.txt
A, please get a gift for C