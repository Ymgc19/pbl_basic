def main():
    num = int(input("num:"))
    print("answer =", factorial(num))

def factorial(num):
    if num < 0:
        return None
    else:
        a = 1
        for _ in range(num, 0, -1):
            a *= _
        return(a)

main()