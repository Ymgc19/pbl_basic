def main():
    num = int(input("num:"))
    print("answer =", factorial(num))

def factorial(num):
    a = 1
    for _ in range(num, 0, -1):
        a *= _
    return(a)

main()
