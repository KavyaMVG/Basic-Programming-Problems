user_input = input("enter a word: ")
reverse = ""
for idx in range(len(user_input)-1, -1, -1):
    reverse = reverse + user_input[idx]
if reverse == user_input:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
