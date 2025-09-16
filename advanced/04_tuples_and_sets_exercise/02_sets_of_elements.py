n_length, m_length = list(map(int, input().split()))
n = set()
m = set()

for _ in range(n_length):
    n.add(int(input()))

for _ in range(m_length):
    m.add(int(input()))

repeats = list(n.intersection(m))
print(*repeats, sep="\n")