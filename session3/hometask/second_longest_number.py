inp = input("input your numbers? ").split()
numbers = []
for num_str in inp:
    numbers.append(int(num_str))

largest = None
second_largest = None

for num in numbers:
    if largest is None or num > largest:
        second_largest = largest
        largest = num
    elif (second_largest is None or num > second_largest) and num != largest:
        second_largest = num

print("Second largest number:", second_largest)