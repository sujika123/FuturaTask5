# Initialize array
arr = [75, 12, 2, 101, 56,45]

# Initialize max with first element of array.
max = arr[0]

# Loop through the array
for i in range(0, len(arr)):
    # Compare elements of array with max
    if (arr[i] > max):
        max = arr[i]

print("Largest element present in given array: " + str(max))
# print(max)
