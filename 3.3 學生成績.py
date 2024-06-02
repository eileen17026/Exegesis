# 預設
total = 0
passed = 0
failed = 0
total_score = 0

# 輸入學生成績
while True:
    score = float(input("請輸入學生成績（輸入 -1 時表示結束）："))
    if score == -1:
        break
    total += 1
    total_score += score
    if score >= 60:
        passed += 1
    else:
        failed += 1

# 全班平均分數
if total > 0:
    average_score = total_score / total
else:
    average_score = 0

# 印出結果
print(f"全班人數: {total}")
print(f"及格人數: {passed}")
print(f"不及格人數: {failed}")
print(f"全班平均分數: {average_score}")