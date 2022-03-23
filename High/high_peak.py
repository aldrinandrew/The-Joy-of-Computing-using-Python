# open file to read input
sample_input = open('sample_input.txt','r')


# open output file to write and append in old file


# To append some text to a file in the end, we first need to open the file with access mode ‘a’,
sample_output = open('sample_output.txt','a')

goodies={}
output_list=[]


# read the input file and strip goodies and values
for f in sample_input:
    index_toRead_price=f.index(":")
    print(f[index_toRead_price+1:].strip())
    print(f[:index_toRead_price])
    goodies[f[:index_toRead_price]]=f[index_toRead_price+1:].strip()
print(goodies)


# prices=list(goodies.values())

prices=[int(i) for i in list(goodies.values())]
# prices_v=list(goodies.values())


# sort the price in descending order it will be easy to distribute the order
prices.sort(reverse=True)
print(prices)


# get the employees
employees=int(input("Number of the employees: "))
print("employees",employees)

length_considered=(len(prices)- employees)

print(length_considered)

for i in range(length_considered):
    maxprice=prices[i]
    minprice=prices[employees+i]
    if i == 0:
        difference=maxprice-minprice
        choosen_index=i
    elif (maxprice-minprice)<difference:
        difference=maxprice-minprice
        choosen_index=i
# find the difference between max and min price

c_price=prices[choosen_index:employees+choosen_index]

difference=max(c_price)-min(c_price)
print("difference",difference)



count=0

for key,value in goodies.items():
    prices[count]
    print(value)
    if int(value) in c_price and count < employees:
        str1=key+": "+value

# append the data in list of order and employees
        output_list.append(str1)
        count+=1
        print(str1)

sample_output.write("Number of employees: "+str(employees))
sample_output.write("\n\n")

# selected goodies
sample_output.write("Here the goodies that are selected for distribution are: ")

sample_output.write("\n")

for i in output_list:
    sample_output.write(i)
    sample_output.write("\n")
sample_output.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(difference))
sample_output.write("\n\n\n")


sample_input.close()
sample_output.close()