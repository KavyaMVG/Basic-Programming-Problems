nums = []

while True:
    user_input = input("Enter a list of numbers: ")

    if user_input.startswith("-") and user_input[1:].isdigit():
        nums.append(int(user_input))

    elif not user_input.isdigit():
        break

    else:
        nums.append(int(user_input))


def min_lst(lst):
    min = lst[0]

    last_idx = len(lst)
    for idx in range(1, last_idx, 1):
        if lst[idx] < min:
            min = lst[idx]
    print(min)


def max_lst(lst):
    max = lst[0]

    last_idx = len(lst)
    for idx in range(1, last_idx, 1):
        if lst[idx] > max:
            max = lst[idx]
    print(max)
