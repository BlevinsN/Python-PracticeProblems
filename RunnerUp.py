if __name__ == '__main__':
    Scores = []
    n = int(raw_input())
    arr = map(int, raw_input().split())
    for x in arr:
        Scores.append(x)
    Scores.sort()
    index = -2
    while Scores[index] == Scores[-1]:
        index -= 1
    print(Scores[index])
