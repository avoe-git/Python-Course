'''
23. Klaviaturadan daxil edilmiş müsbət tam ədədin rəqəmlərinin cəmini və hasilini tapan proqram tərtib edin.
'''

a = int(input())
b=0
g=1
for i in range(len(str(a))):
    b=b+int(str(a)[i])
    g = g*int(str(a)[i])
print('Rəqəmlərinin cəmi:',b,'| Rəqəmlərinin hasili:', g)