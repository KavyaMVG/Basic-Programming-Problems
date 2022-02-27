def caesar_cipher(word, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_word = ""

    for idx in range(len(word)):
        letter = word[idx]
        updated_idx = (alphabet.index(letter) + key) % 26
        encrypted_word = encrypted_word + alphabet[updated_idx]
    return encrypted_word


file = open("MyFile.txt", "r")
files_content = file.read().split("\n")
file.close()

encrpyted_words = ''

for password in files_content:
    word, key = password.split(" ")
    key = int(key)
    encrpyted_words += caesar_cipher(word, key) + '\n'

file = open("encrpyted-password.txt", 'w')
files_content = file.write(encrpyted_words)
file.close()
