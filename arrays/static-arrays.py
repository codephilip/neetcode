# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity.
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n


# Remove from the last position in the array if the array
# is not empty (i.e. length is non-zero).
def removeEnd(arr, length):
    if length > 0:
        # Overwrite last element with some default value.
        # We would also consider the length to be decreased by 1.
        arr[length - 1] = 0


# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.
def insertMiddle(arr, i, n, length):
    # Shift starting from the end to i.
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]

    # Insert at i
    arr[i] = n


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
