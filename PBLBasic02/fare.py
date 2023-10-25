def main():
    age = int(input("age:"))
    print("fare:", get_fare(age))

def get_fare(age):
    if age <= 9:
        return(100)
    elif age >= 10 and age <= 17:
        return(150)
    return(250)

main()
