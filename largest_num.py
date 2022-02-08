num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print(f"Greatest is {num1}")
if num2 > num1 and num2 > num3:
    print(f"Greatest is {num2}")
if num3 > num1 and num3 > num2:
    print(f"Greatest is {num3}")


# nums = list(map(int, input().split(" ")))
# print(max(nums))


# nums = list(map(int, ['1', '2', '3']))
# print(nums)
