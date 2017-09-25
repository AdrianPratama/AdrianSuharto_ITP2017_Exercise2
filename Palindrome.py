word = input("Please input the word here:")
word_list = list(word)
if word_list == list(reversed(word_list)):
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
