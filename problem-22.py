'''
22. Klaviaturadan daxil edilən n rəqəmli natural ədədin armstronq ədəd olub-olmadığını yoxlayan proqram tərtib edin.
'''

a = int(input())
b=0
for i in range(len(str(a))):
    b = b + pow(int(str(a)[i]),len(str(a)))
if b == a:
    print('Armstronq ədədir')
else: 
    print('Armstronq ədədi deyil')