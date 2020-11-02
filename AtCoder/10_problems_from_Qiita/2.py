# 標準入力をリスト化
s_list = list(input())
# 文字列のリストを数値のリストに変換
sss = [int(s) for s in s_list]
i = 0
for x in sss:
  if x == 1:
    i+=1

print(i)