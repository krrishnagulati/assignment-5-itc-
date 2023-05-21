# QUESTION 6
'''Write a python program to print the prime numbers for a user input range.'''      

starting = int(input("Enter the starting number: "))
ending = int(input("Enter the ending number: "))

print(f"Prime numbers between {starting} and {ending}:")
for num in range(starting, ending + 1):
    if num > 1:
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num)

