S = input()

min_result = max_result = prev = S
curr = ''

for i in range(len(S)):
    curr = prev[1:] + prev[0]
    prev = curr
    if min_result > curr:
        min_result = curr
    elif max_result < curr:
        max_result = curr

print(min_result)
print(max_result)
