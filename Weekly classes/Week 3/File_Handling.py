"""
Theory of Evolution
Concept of file handling in Python
    r+ mode for both read and write
    w mode for write
    r is the read mode
    a is appending mode
"""


with open("hello.txt","r+") as myfile:

    print(myfile.read())
    myfile.write("I am fine")
myfile.close