"""
Given two numbers (integers) as input, print the smaller number.

Input Format:
The first line of input contains two numbers separated by a space

Output Format:
Print the smaller number

Example:

Input:
2 3

Output:
2
"""

a, b = input().split(" ")
a = int(a)
b = int(b)
if a < b:
    print(a)
else:
    print(b)
