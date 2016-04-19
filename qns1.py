arr = [1,2,2,4,5,5,2]
#Question 1
counter = 0
for i in range(len(arr)):
    times = 0
    while i in arr:
        arr.remove(i)
        times += 1
    if times > 1:
        counter += 1
print(counter)
