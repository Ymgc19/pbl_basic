def main():
    values = [5, -2, 0, 3, -4]
    print(remove_minus(values)) # 5, 0, 3 が表示されればOK

def remove_minus(values):
    new_list = []
    for _ in values:
        if _ >= 0:
            new_list.append(_)
    return new_list

main()
