'''
21. Klaviaturadan daxil edilən üçrəqəmli ədədin armstronq ədəd olub-olmadığını yoxlayan proqram tərtib edin.
(Əgər n-rəqəmli ədədin rəqəmlərinin n-ci qüvvətlərinin cəmi həmin ədədin özünə bərabərdirsə, belə ədəd Armstronq ədədi adlanır. 
Məsələn, 1634=1^4+6^4 +3^4 + 4^4, 153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3 )
'''

a = int(input())
b=0
for i in range(len(str(a))):
    b = b + pow(int(str(a)[i]),len(str(a)))
if b == a:
    print('Armstronq ədədir')
else: 
    print('Armstronq ədədi deyil')