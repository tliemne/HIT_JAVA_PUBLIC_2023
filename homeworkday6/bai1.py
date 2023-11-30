def MyMultiple(a):
    res = 1
    for i in a:
        res *= i
    return res
if __name__ == "__main__":
    print(MyMultiple(map(float, input().split())))