a,b = map(int, input().split())
i = 1

while a >= i * b:
    i += 1
else:
    print(i - 1)