my_file = open('MyFile.txt', 'r')
content = my_file.read()
my_file.close()

content = list(map(int, content.split("\n")))

res = ''
for num in content:
    if num % 2 == 0:
        res = res + str(num) + "\n"

file = open('MyFile.txt', 'w')
file.write(res)
file.close()
