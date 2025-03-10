hi = "Hello"
who = "World"

print(hi + " " + who)  # Hello World
print(hi + who[:3] + who[4:])  # HelloWord
print(hi + " " + who[:3] + who[4:])  # Hello Wor d
print((hi + who).upper())  # HELLOWORLD
print("racecar"[::-1])  # racecar

print((3 * (hi + " ") + 5 * (who + ",")).replace(",", " ").split(" "))
# ['Hello', 'Hello', 'Hello', 'World', 'World', 'World', 'World', 'World', '']

import string

def clean_string(s):
    """Removes punctuation and converts to lowercase."""
    return s.translate(str.maketrans("", "", string.punctuation)).replace(" ", "").lower()

def is_palindrome(s):
    """Check if a string is a palindrome."""
    cleaned = clean_string(s)
    return cleaned == cleaned[::-1]

# Input
phrase = input("Enter a sentence: ")

# Check palindrome
if is_palindrome(phrase):
    print("✅ This is a palindrome!")
else:
    print("❌ This is NOT a palindrome.")