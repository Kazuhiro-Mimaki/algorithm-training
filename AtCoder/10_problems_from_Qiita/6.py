N = int(input())
a_list = list(map(int,input().split()))
a_list.sort(reverse=True)

i = 0
Alice = []
Bob = []

for i in range(len(a_list)):
  if i % 2 == 0:
    Alice.append(a_list[i])
  else:
    Bob.append(a_list[i])

result = sum(Alice) - sum(Bob)
print(result)