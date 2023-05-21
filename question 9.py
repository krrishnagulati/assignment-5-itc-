#QUESTION 9
'''Write a program to count the number of occurrences of each word in the 
list(List entered by the user).'''

word_list = input("Enter a list of words : ").split()
# split (string gets splitted to list)
word_counts = {}
for word in word_list:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("Word counts:")
for word, count in word_counts.items():
    print(f"{word} : {count}")
