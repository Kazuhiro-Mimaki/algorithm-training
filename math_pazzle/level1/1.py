
for i in range(10, 1000):
  # 10進数
  num = i
  num = str(num)
  num_list = list(num)
  num_reverse_list = num_list[::-1]
  # 2進数
  num_to_b = format(i, "b")
  num_to_b = str(num_to_b)
  num_list_b = list(num_to_b)
  num_reverse_list_b = num_list_b[::-1]
  # 8進数
  num_to_o = format(i, "o")
  num_to_o = str(num_to_o)
  num_list_o = list(num_to_o)
  num_reverse_list_o = num_list_o[::-1]

  if num_list == num_reverse_list and num_list_b == num_reverse_list_b and num_list_o == num_reverse_list_o:
    print(f"{num} true")