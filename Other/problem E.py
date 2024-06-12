f = [58, 96649, 1029, 773, 211]
g = []

for i in range(len(f)):
    for x in str([i]):
        if int(x) % 2 == 0:
            cemi= cemi + int(x)
    g.append(cemi)

print(f[g.index(max(g))])