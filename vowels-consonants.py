user_input = input("Enter a word: ")
vowel_count = 0
consonants_count = 0
for idx in range(len(user_input)):
    char = user_input[idx]
    if char in "aeiou":
        vowel_count = vowel_count + 1
    else:
        consonants_count = consonants_count + 1

print("vowel count:  ", vowel_count)
print("consonants count:  ", consonants_count)
