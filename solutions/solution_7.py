"""
Solution for problem #7 [Generated by avoe's afs.py]

Statement of the problem:
Bomboclat
"""

a=[]
b=[]
c=[]
x = int(input())
for i in range(1, x+1):
    a.append(int(input()))
for i in range(1, x+1):
    b.append(int(input()))
for i in range(1, x+1):
    c.append(a[i-1]+b[i-1])
print(c)