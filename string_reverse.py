word = input("Enter a word: ")
reverse = ""

for char in range(len(word)-1, -1, -1):
    reverse = reverse + word[char]
print(reverse)
