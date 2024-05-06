s = list(input().split(' '))
f=[]

for i in range(len(s)):
    f.append(s[i].count('c'))

print(s[f.index(max(f))])