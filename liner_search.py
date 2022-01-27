def liner_search(data, value):
  for i in range(len(data)):
    if data[i] == value:
      return i
  return -1

data = [50, 30, 90, 10, 20, 70, 50, 40, 80]
print(liner_search(data, 20))