#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
x = str(input("Enter a word: ")).strip()
y = str(input("Enter a word: ")).strip()
z = str(input("Enter a word: ")).strip()
a = str(input("Enter a word: ")).strip()
b = str(input("Enter a word: ")).strip()

l = []

l.append(x)
l.append(y)
l.append(z)
l.append(a)
l.append(b)
print(l)