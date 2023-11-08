def main():
    profit = int(input("profit:"))
    sales = int(input("sales:"))
    print("利益率は", rate(profit, sales), "%です")

def rate(profit, sales):
    return (profit*1000 // sales) / 10


main()