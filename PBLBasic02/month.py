def main():
    month = int(input("month:"))
    print("days:", get_month_days(month))

def get_month_days(month):
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]

    if month in thirty_one:
        return(31)
    elif month in thirty:
        return(30)
    return(28)

main()
