def main():
    num = int(input("num:"))
    print("answer =", factorial(num))

def factorial(num):
    ans = 1
    for _ in range(num, 0, -1):
        ans *= _
    return(ans)

main()
