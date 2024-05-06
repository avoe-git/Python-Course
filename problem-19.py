'''
19. Klaviaturadan daxil edilən ədədin polindrom olub-olmadığını yoxlayan proqram tərtib edin.
(Düzünə və tərsinə eyni cür oxunan ədədlər palindrom ədədlər adlanır. Məsələn, 222, 5775 və s.)
'''

a = int(input())
if str(a)[::-1]==str(a):
    print('Polindromdur')
else:
    print('Polindrom deyil')