#QUESTION 4
'''Write a Python program to construct the following pattern, using a nested for loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
rows =5
for i in range(1, rows + 1):
        for j in range(1, i + 1):     # here star patter is increasing
            print("*", end=" ")         #END HELPS US TO GET STAR ALONG ONE ROW
        print()                       # this print () helps us to get to next row
for i in range(rows - 1, 0, -1):        # here we have given beginning,termination,and decrement respectively
        for j in range(1, i + 1):      # here star pattern is decreasing
            print("*", end=" ")
        print()                        # this print () helps us to get to next row
