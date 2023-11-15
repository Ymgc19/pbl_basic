def main():
    data = [10, 30, -20, 40]
    print(contains_minus(data))  # Trueが表示されればOK

    data = [10, 30, 40]
    print(contains_minus(data))  # Falseが表示されればOK

# ヒントを見てもいいコードが思いつかなかったので，面倒なコードを書いてしまいました．

def contains_minus(values):
    x = 1
    for _ in values:
        if _ < 0:
            x *= 0
    if x == 0:
        return True
    return False
main()
