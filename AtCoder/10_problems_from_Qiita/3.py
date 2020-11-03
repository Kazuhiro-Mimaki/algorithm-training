n = int(input())
a_list = input().split()
a_list = [int(a) for a in a_list]
res = 0
exist_odd = False

while True:
  for a in a_list:
    if a % 2 != 0:
      exist_odd = True
      print(exist_odd)
  if exist_odd == True:
    break
  for a in a_list:
    if a % 2 == 0:
      a /= 2
      print(a)
  res+=1
print(res)