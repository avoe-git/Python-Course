'''
31. Sətir tipli verilənləri ədəd tipinə çevirən proqram tərtib edin. Bildiyiniz
kimi, input() funksiyası klaviaturadan daxil edilən kəmiyyətin tipindən
asılı olmayaraq, həmişə sətir qaytarır. Aşağıda təyin olunan yeni
num_input() funksiyasının qaytardığı qiymət isə ədəd olur.
'''

def num_input(a):
    print(int(a))

num_input(input())