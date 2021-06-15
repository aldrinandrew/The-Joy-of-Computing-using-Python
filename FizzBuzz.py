"""
  If a number is a multiple of 3......print Fizz
  If a number is a multiple of 5......print Buzz
  If the number is the multiple of 3 & 5 ......print FizzBuzz

"""

def fizz_buzz(r):
    for i in range(1,r):
        if(i%3==0 and i%5==0):
            print(str(i),"FIZZ..BUZZ..")
        elif(i%3==0):
            print(str(i),"FIZZ...")
        elif(i%5==0):
            print(str(i),"BUZZ...")
        else:
            print(i)

fizz_buzz(101)