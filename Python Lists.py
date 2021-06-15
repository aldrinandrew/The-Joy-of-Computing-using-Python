#PART1- INTRODUCTION
#List_ Lists are Flexible Data Structure in which you can add and delete items easily

shopping = ["Bread","Coffee","Sugar"]
print(shopping)
for item in shopping:
    print(item)

#Append_ Adding to the end

shopping.append("Curd")
print(shopping)

# PART-2 LIST MANIPULATION

#Index is the position of items in the list

print(shopping[0])
print(shopping[1])
print(shopping[2])
print(shopping[3])

print("Another ways")

for i in range(4):
    print(shopping[i])

# Name.....Student information lists can be easily handy
#Student1
#Student2


print("I want to change the order as, Bread, Oil, Coffee, Sugar, Curd ")

#insert command automatically insert the item into the desired index

shopping.insert(1,"Oil")
print("Oil inserted")
for item in shopping:
    print(item)

#If you have census data there will be repitation

ages = [21,84,8,61,6,31,31,8,55,45,45,6,3,1,11,12,12,22,25,25,15,25]

#How many  people of age 25 are living?

print(ages.count(25))
print(ages.count(12))
print(ages.count(99))

print(len(ages))
print(len(shopping))

#Limit the printing items in a list using for loop range

for i in range(2):
    print(shopping[i])

#PART-3 LIST OPERATORS

print(ages)

# If the list is sorted we can get an idea

# Sorting Algorithm Technique_ Bubble Sort, Quick Sort, Merge Sort

#Here we are not using any of these algorithm
ages.sort()
print(ages)

#Reverse sorting

ages.reverse()
print(ages)



# Considering students data set

students = ["Arun","Rajesh","Harish","Akanksha","Lakshmi","Varsha"]
print(students)
students.sort()
print(students)


#If you want to assign the roll numbers, you can insert some dummy value to the list in index 0

students.insert(0,"Dummy")
print(students)

# SLICING IS THE OPERATION IN WHICH YOU CAN GET A SUBSET OF THE LIST

# PART- 4 SLICING

# list_name[start_index:end_index+1]  is the syntax

print(students[1:5])


print(students[:])     # Take the entire values


print(students[3:])

print(students[:5])


# Default start index is zero and default end index i length of the list










