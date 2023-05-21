# QUESTION 2
'''Python Program to Print all Numbers in a Range Divisible by a Given Number. (user inputs
the range and the number)'''


num1 = int(input("enter the beginning for a range:"))
num2 = int(input("enter the termination for a range:"))
# here num1,num2 are variables which defines the range
num3 = int(input("enter the number whose divisible we want to extract from range:"))
# num3 is a variable which defines the number for which we want divisibles in the user entered range
for number in range(num1,num2+1):
     if number%num3==0:
          print(number)
