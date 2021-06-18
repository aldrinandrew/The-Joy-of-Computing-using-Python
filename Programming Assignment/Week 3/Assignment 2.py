"""

Given a list of numbers (integers), find second maximum and second minimum in this list.

Input Format:
The first line contains numbers separated by a space.

Output Format:
Print second maximum and second minimum separated by a space

Example:
Input:
1 2 3 4 5

Output:
4 2

"""


lst = [int(i) for i in input().split(" ")]
lst.sort()
print(lst[-2], lst[1])
