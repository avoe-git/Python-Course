'''
28. Klaviaturadan soyad və adınızı boşluq simvolu ilə daxil edin. Daha
sonra soyad və adın yerini dəyişən proqram yazın. Məsələn, giriş -
Kərimov Kərim, çıxış – Kərim Kərimov
'''

print(' '.join(list(input().split(' '))[::-1]))