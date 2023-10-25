def main():
    num = int(input())
    if num <= 0:
        print("Error")
        return
    total = 0
    for i in range(1, num + 1):
        total += i
    print("Total:", total)

main()
