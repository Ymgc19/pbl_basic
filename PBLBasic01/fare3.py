sum = 0
for _ in range(3):
    age = int(input("年齢: "))
    if age <= 9:
        print("100 yen")
        sum += 100
    else:
        print("150 yen")
        sum += 150
print(sum, "yen")