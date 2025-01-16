n = int(input())
s = 0
for i in range(1,n+1,2):
    s = s+(1/i)**i
print(s)