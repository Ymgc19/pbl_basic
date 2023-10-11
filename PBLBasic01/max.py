def main():
    values = [20, -80, 40, 90, 50]
    print("max:", max2(values))            # 90が表示されればOK

def max2(values):
    a = values[0]
    for _ in range(len(values) - 1):
        if values[_+1] > a:
            a = values[_+1]
    return a

main()

