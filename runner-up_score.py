if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr = [scores for scores in arr if scores != max(arr)]
    print(max(arr))
