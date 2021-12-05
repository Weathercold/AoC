inp = list(map(int, open(r".\2021\input\d1-sonar-sweep.txt").readlines()))
print(sum([1 if inp[i] > inp[i-1] else 0 for i in range(1, len(inp))]))
print(sum([1 if sum(inp[i-2:i+1]) > sum(inp[i-3:i]) else 0 for i in range(3, len(inp))]))