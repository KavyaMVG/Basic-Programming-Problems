
linear_list = list(map(int, input().split(" ")))
print(linear_list)


target = int(input("Enter number from 1 to 10: "))


for idx in range(len(linear_list)):
    search = linear_list[idx]
    if search == target:
        print(f"Found at position {idx +1}")
        break
