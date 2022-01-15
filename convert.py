# n = 18
# result = ''

# while n > 0:
#     result = str(n % 2) + result
#     n //= 2
# print(result)


# n = '10010'
# result = 0

# for i in range(len(n)):
#     result += int(n[i]) * (2 ** (len(n) - i -1))
# print(result)

a = 18
print(bin(a))

b = '10010'
print(int(b, 2))