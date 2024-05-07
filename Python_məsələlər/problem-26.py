'''
26. Klaviaturadan daxil edilmiş müsbət tam ədədin rəqəmlərinin artan
sıra ilə düzüldüyünü müəyyən edən proqram tərtib edin.
'''

a = list(map(int,input()))
blist = a.copy()
blist.sort()
if blist == a:
    print('Sıra ilə düzülmüşdür')
else:
    print('Sıra ilə düzülməmişdir')