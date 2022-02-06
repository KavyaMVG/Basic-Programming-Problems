user_input = input("Enter a word: ")

character_count = {}


for idx in range(len(user_input)):
    char = user_input[idx]

    if char not in character_count:
        character_count[char] = 1
    else:
        character_count[char] = character_count[char] + 1
print(character_count)
