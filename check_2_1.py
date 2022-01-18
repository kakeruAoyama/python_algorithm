# 自己解答
for i in range(1900, 2050):
  if i % 4 == 0:
    if i % 100 == 0 and i % 400 != 0:
      continue
    print(i, end=' ')