a,b = input().split()
a = int(a)
b = int(b)
result = a * b % 2
if result == 0:
  print('Even')
else:
  print('Odd')