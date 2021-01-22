# NumPyとは多次元配列を効率的に扱うライブラリ
import numpy as np
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
A = np.array(A)
print(np.sum(A - np.min(A)))