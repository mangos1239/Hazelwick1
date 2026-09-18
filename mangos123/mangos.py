word= input("Enter a word")
wordreverse = word[::-1]
print(word[::-1])
print(word.upper())
length_word=len(word)
Palindrome = word == wordreverse
print("palindrome:",Palindrome)