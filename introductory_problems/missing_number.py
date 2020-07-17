# we didn't followed that approach where we go the current number's indices and make it negative to indicate as its visited(firstDuplicate problem) , as we have one less number (N-1 numbers in array)
n = int(input())
array = list(map(int, input().split()))
s = 0

for i in range(len(array)):

    s += array[i]

print(n * (n+1) // 2 - s)
