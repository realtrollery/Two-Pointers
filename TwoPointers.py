arr = [1, 2, 3, 4, 2, 5, 3, 1, 1, 2, 99]
targetVal = 102
n = len(arr)
end = 0
cnt = 0
sumOfRange = 0
for start in range(n):
    while end < n and sumOfRange < targetVal:
        sumOfRange += arr[end]
        end += 1
    if sumOfRange == targetVal:
        print(start, end - 1)
        exit()
    sumOfRange -= arr[start]
