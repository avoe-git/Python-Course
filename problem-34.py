'''
34. Verilmiş natural ədədin sağdan üçüncü rəqəmini çıxışa verin. Bu
proqramda dövrün 3 dəfə yerinə yetirilməsi bəs edir. Ona görə də for
dövründən istifadə olunur.
'''
k=int(input())
k = list(str(k))
k.pop(-2)
print(''.join(k))