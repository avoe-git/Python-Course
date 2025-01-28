n = int(input())
summ = 0
while n>0:
    summ = summ + str(n).count('1')
    n -= 1
print(summ)