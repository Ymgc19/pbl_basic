def main():
    profit = int(input("profit:"))
    sales = int(input("sales:"))
    print("利益率は", rate(profit, sales), "%です")

def rate(profit, sales):
    x = ((profit*10000 // sales)) + 5
    return x // 10 / 10

main()