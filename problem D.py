a = int(input())
c, b, g =[], [], []

for i in range (len(str(a))):
    q = a%10
    c.append(q)
    a = a//10
c.sort()

for i in range(len(c)):
    if c.count(min(c)+1) > 0:
        c.remove(min(c)+1)
        c.insert(0, min(c)+1)

for i in range(len(c)):
    g.append(str(c[i]))
    
print("".join(g))