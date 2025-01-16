n = int(input())
k = 0
for i in range(len(str(n))):
    k = k+int(str(n)[i])
if n%k==0:
    print('Bolunur')
else:
    print('Bolunmur')