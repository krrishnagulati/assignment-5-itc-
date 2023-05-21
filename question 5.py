#QUESTION 5
'''Write a python program to print a triangular pattern of the alphabet (user input the
number of rows).
Example: Input the number of rows = 5, then the pattern should come out as given below.
If the count of the alphabet gets exhausted, repeat the alphabet from A.

A
BC
DEF
GHIJ
KLMNO'''


current_letter =0
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rows = int(input("enter the no of rows:"))
for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(alphabet[current_letter % len(alphabet)], end="")
            current_letter += 1
        print()