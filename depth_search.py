tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [], [], [], [], [], [], [], [],]

# 行きがけ順
def serch(pos):
  print(pos, end=' ')
  for i in tree[pos]:
    serch(i)
serch(0)