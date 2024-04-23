# size of arr is 4
arr = [1, 2, 3, 4, 5]
print("length of arr:", len(arr))

# Traversing through arr.
for i in range(len(arr)):
    print("index:", i)
    print("val:", arr[i])

# OR

i = 0
while i < len(arr):
    print(arr[i])
    i += 1


# Range function
numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers)):
    print(f"Index {i}, Value {numbers[i]}")

numbers = [10, 20, 30, 40, 50]
# Start at the second element and print each one
for i in range(1, len(numbers)):
    print(f"Index {i}, Value {numbers[i]}")

# Enumerate
numbers = [10, 20, 30, 40, 50]
for i, value in enumerate(numbers):
    print(f"Index {i}, Value {value}")

for i, value in enumerate(numbers, 1):
    print(f"Index {i}, Value {value}")
