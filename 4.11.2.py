def is_odd(x):

    if x % 2 == 1:
        return True
    else:
        return False

# 輸入數字
x = int(input("請輸入一個整數："))
print("您輸入的數字是否為奇數：", is_odd(x))