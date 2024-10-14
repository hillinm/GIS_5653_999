data = ((1, 2), (3, 4))

index = 1
for i in data:
    print(f"Row {index} sum: {sum(i)}")
    index += 1

numbers = [4, 3, 2, 1]
print(numbers)

numbers_copy = numbers[:]
print(numbers_copy)

numbers.sort()
print(numbers)