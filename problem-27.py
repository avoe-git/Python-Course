'''
27. Klaviaturadan daxil edilmiş müsbət tam ədəddə 2 və 7 rəqəmlərini
silən proqram tərtib edin. (Məsələn, girişdə 12457847, çıxışda 14584)
'''

print(''.join(list(filter(lambda x: x!='2' and x!='7', list(input())))))