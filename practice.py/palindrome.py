word = input("Enter anything to check: ")

if word == word[::-1]:
    print("It is a palindrome")

else:
    print("It is not a palindrome")