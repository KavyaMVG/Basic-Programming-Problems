
num = int(input("Enter number:"))

flag = False

if num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            flag = True
            break
if flag:
    print("its not prime number")
else:
    print("its a prime number")
# x = 0
# while x < 5:
#     print(x)
#     x = x + 1
