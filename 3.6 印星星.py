n = 3 

# 上半部分123
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# 下半部分45
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))