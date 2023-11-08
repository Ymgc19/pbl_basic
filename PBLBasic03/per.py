def main():
    num1 = int(input("num1:"))
    num2 = int(input("num2:"))
    num3 = int(input("num3:"))
    num4 = int(input("num4:"))
    num5 = int(input("num5:"))
    return(percent(num1, num2, num3, num4, num5))


def rate(a, b):
    return (b*1000 // a) / 10

def percent(num1, num2, num3, num4, num5):
    num_list = [num1, num2, num3, num4, num5]
    total = sum(num_list)
    for _ in range(5):
        print("{} {}%".format(num_list[_], rate(total, num_list[_])))
    print("-----------")
    print("{}".format(total), "100.0%")

main()