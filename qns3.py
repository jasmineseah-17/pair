#Question 3
num = 6
counter = 0
for i in range(len(arr)):
    if num == arr[i]:
        print("In array")
    else:
        counter += 1
if counter == len(arr):
    print("not in array")

#OR
swapped = True
for i in range(len(arr)):
    if num == arr[i]:
        print("In array")
        swapped = False
if swapped:
    print("not in array")
