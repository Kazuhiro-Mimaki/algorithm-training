A = input()
B = input()
C = input()
X = input()
A = int(A)
B = int(B)
C = int(C)
X = int(X)

sum = 0
i = 0
j = 0
for i in range(A+1):
  for j in range(B+1):
    for k in range(C+1):
      if i*500 + j*100 + k*50 == X:
        sum += 1
print(sum)

