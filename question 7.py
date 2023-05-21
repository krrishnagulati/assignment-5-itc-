#QUESTION 7
'''Write a python program to find the numbers which are multiple of 7
and divisible by 11 in the range 1-500.'''

for i in range(1,501):
    if (i%7==0 and i%11==0):
        print(i)
        

