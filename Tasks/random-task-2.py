a = int(input())
for i in str(a):
    if int(i)>=0 and int(i)<8:
        test=True
    else:
        test=False
        break
print(test)