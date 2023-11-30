def tong(arr, x):
    sum = 0
    for i in range(0, x + 1):
        sum += arr[i]
    return sum


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    t = int(input())
    for i in range(0, t):
        x = int(input())
        print(tong(arr, x))