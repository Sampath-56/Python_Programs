word = input("Enter a word: ")
if word == word[::-1]:
    print(" it's a palindrome!")
else:
    print(" it's not a palindrome.")