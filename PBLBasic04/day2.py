# 日数入力
date = int(input("日付:"))

# -1が出たらbreak，日数が一定の範囲を超えたらbadでbreak
while date != -1:
    if date > 30 or date < 1:
        print("Bad"); break
    print("the day is", (date+2) % 7)
    date = int(input("日付:"))