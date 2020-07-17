s = input()
count = 1
result = 1
# ACCGGGTTTT

match = s[0]

for i in range(1, len(s)):
    if s[i] == match:
        count += 1
        result = max(result, count)

    else:
        match = s[i]
        count = 1

print(result)
