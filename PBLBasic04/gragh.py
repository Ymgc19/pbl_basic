values = []
for i in range(5):
    value = int(input("value:"))
    values.append(value)

total = sum(values)
ruikei = 0
prev_rate = 0
for value in values:
    ruikei += value
    ruikei_rate = ruikei * 100 * 100 // total   # 累計の割合を求める
    ruikei_rate = (ruikei_rate + 5) // 10       # 四捨五入する
    curr_rate = ruikei_rate - prev_rate         # 個々の割合を求める
    print("{:4d} {:3d}.{:d}%".format(value, curr_rate//10, curr_rate%10))
    prev_rate = ruikei_rate
print("-----------")
print("{:4d} 100.0%".format(total))

