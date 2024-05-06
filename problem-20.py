'''
20. Klaviaturadan daxil edilən sətrin polindrom olub-olmadığını yoxlayan proqram tərtib edin.
(Düzünə və tərsinə eyni cür oxunan sözlər palindrom sözlər adlanır. Məsələn, qapaq, ənənə, və s.)
'''

a = input()
if a[::-1] == a:
    print('Polindromdur')
else: 
    print('Polindrom deyil')