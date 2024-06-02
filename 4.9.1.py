def compare_value(x, y):
  
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1

# 輸入兩個數字
x = float(input("x="))
y = float(input("y="))

# 比較兩個數字並輸出結果
result = compare_value(x, y)
print("結果：", result)
