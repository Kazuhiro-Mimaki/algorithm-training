N,Y = map(int,input().split())
result = [-1, -1, -1]

for x in range(N):
  for y in range(N-x):
    z = N-x-y
    sum = 10000*x + 5000*y + 1000*z
    if sum == Y:
      result = [z, y, z]

print(result)