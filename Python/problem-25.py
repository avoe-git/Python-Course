'''
25. 1000 və 10000 aralığnda 1-dən 9-a qədər rəqəmlərin hər birinə tam
bölünən ədədləri ekranda əks etdirən proqram tərtib edin.
'''

a = 1001
while 1000 < a < 10000:
    if a%1 == 0 and a%2 == 0 and a%3==0 and a%4==0 and a%5 == 0 and a%6==0 and a%7==0 and a%8==0 and a%9==0:
        print(a)
    a+=1