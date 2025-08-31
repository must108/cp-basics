# understanding time complexity

def maxSubarraySumn3(inp):
    best = 0
    n = len(inp)

    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(i, j+1):
                s += inp[k]
            best = max(best, s)

    return best

def maxSubarraySumn2(inp):
    best = 0
    n = len(inp)

    for i in range(n):
        s = 0
        for j in range(i, n):
            s += inp[j]
            best = max(best, s)

    return best

# Kadane's Algorithm
def maxSubarraySumDP(inp):
    best = 0
    s = 0

    n = len(inp)

    for i in range(n):
        s = max(inp[i], s + inp[i])
        best = max(best, s)

    return best

def main():
    inp = [-1, 2, 4, -3, 5, 2, -5, 2]

    print(maxSubarraySumn3(inp))
    print(maxSubarraySumn2(inp))
    print(maxSubarraySumDP(inp))


if __name__ == "__main__":
    main()