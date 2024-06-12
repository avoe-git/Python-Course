'''
1. Rəqəmləri cəmi daxil edilmiş natural ədədə bərabər olan bütün
ikirəqəmli ədədlərin sayını ekranda çap edin.
'''

f=int(input())
x=0
for i in range(10,100):
    if int(str(i)[1])+int(str(i)[0])==f:
        x=x+1
print(x)