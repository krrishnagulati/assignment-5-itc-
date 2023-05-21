#QUESTION 8
'''Input 10 integer values from the user. Write a python program to find
 and print the following:

a. positive numbers
b. negative numbers
c. odd numbers
d. even numbers
e. Number of times each number occurs in the List 
'''

# creating empty lists for different categories
positive_numbers = []
negative_numbers = []
odd_numbers = []
even_numbers = []

# creating an empty dictionary to store number occurrences
number_occurrences = {}

print("Enter 10 integer below:-")
for _ in range(10):
    num = int(input("Enter an integer value: "))


    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)

    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

    # Counting  the number occurrences
    if num in number_occurrences:
        number_occurrences[num] += 1
    else:
        number_occurrences[num] = 1


print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

print("Number occurrences:")
for num, count in number_occurrences.items():
    print(f"{num} : {count}")
