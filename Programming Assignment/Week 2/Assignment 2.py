"""
In this assignment, you will have to take two numbers (integers) as input and print the addition.

Input Format:

The first line of the input contains two numbers separated by a space.

Output Format:

Print the addition in single line

Example:

Input:
4 2

Output:
6
"""

a, b = input().split(" ")   # Taking multiple input from the user. Cannot convert it directly to integer
a = int(a)
b = int(b)
print(a+b)