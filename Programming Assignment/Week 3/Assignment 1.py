"""
You all have seen how to write loops in python. Now is the time to implement what you have learned.

Given an array A of N numbers (integers), you have to write a program which prints the sum of the elements of array A with the corresponding elements of the reverse of array A.
If array A has elements [1,2,3], then reverse of the array A will be [3,2,1] and the resultant array should be [4,4,4].

Input Format:

The first line of the input contains a number N representing the number of elements in array A.
The second line of the input contains N numbers separated by a space. (after the last elements, there is no space)

Output Format:

Print the resultant array elements separated by a space. (no space after the last element)

Example:

Input:
4
2 5 3 1

Output:
3 8 8 3

Explanation:
Here array A is [2,5,3,1] and reverse of this array is [1,3,5,2] and hence the resultant array is [3,8,8,3]

# Basic example to take input from to the list

lst = []
n = int(input("Enter the number of inputs: "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)

print(lst)


# Use map function to take input in single line

n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the values").strip().split()))


# Use below to take input excluding space in last

n = int(input("Enter the number of elements: "))
a = [int(i) for i in input().split(" ")]
print(a)

"""

n = int(input("Enter the number of elements"))
a = [int(i) for i in input().split(" ")]
b = []
for i in range(len(a)-1, -1, -1):             # Reversing the list using for loop
    b.append(a[i])
c = []
for i in range(len(b)):
    c.append(a[i]+b[i])

for i in range(len(c)):
    if i == len(c)-1:
        print(c[i])
    else:
        print(c[i], end=" ")