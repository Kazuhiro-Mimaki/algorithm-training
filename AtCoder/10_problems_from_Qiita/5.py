N,A,B=map(int,input().split())
ans = 0
i = 1
for i in range(N):
  sum = 0
  x = i
  for j in range(5):
    sum += x%10
    x /= 10
  if sum >= A and sum <= B:
    ans += i
print(ans)