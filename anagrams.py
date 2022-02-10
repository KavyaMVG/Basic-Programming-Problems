word1 = input("Enter word: ")
sort_word1 = sorted(word1)
delimiter = ""
sort_word = delimiter.join(sort_word1)

word2 = input("Enter word: ")
sort_word2 = sorted(word2)
sort_word = delimiter.join(sort_word2)

if word1 == word2:
    print(True)
else:
    print(False)
