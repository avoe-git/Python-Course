'''
24. Klaviaturadan daxil edilmiş müsbət tam ədədin cüt rəqəmlərinin cəmini və hasilini tapan proqram tərtib edin.
'''

a = int(input())
b=0
g=1
for i in range(len(str(a))):
    if int(str(a)[i])%2 == 0:
        b=b+int(str(a)[i])
        g = g*int(str(a)[i])
print('Cüt rəqəmlərinin cəmi:',b,'| Cüt rəqəmlərinin hasili:', g)