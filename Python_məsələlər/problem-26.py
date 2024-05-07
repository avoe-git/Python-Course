'''
26. Klaviaturadan daxil edilmiş müsbət tam ədədin rəqəmlərinin artan
sıra ilə düzüldüyünü müəyyən edən proqram tərtib edin.
'''

a = list(map(int,input()))
blist = a.copy()
if blist.sort() == a:
    print('Sıra ilə düzülmüşdür')
else:
    print('Sıra ilə düzülməmişdir')