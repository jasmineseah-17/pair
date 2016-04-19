#Question 4a and b)
highest = 0
lowest = 9999999
for i in range(len(arr)):
    if arr[i] > highest:
        highest = arr[i]
    if lowest > arr[i]:
        lowest = arr[i]
print(highest)
print(lowest)
