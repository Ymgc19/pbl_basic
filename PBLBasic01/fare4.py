sum = 0
for _ in range(3):
    age = int(input("年齢: "))
    if age <= 9:
        print("100 yen")
        sum += 100
    elif age >= 10 and age <= 17:
        print("150 yen")
        sum += 150
    else:
        print("250 yen")
        sum += 250
print(sum, "yen")