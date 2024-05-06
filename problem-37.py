'''
37. Sətrin düz ortasında yerləşən simvolu çıxışa verin. Əgər simvolların
sayı cütdürsə, ortadakı iki simvolu çıxışa verin.
'''
x = input()
if len(x)%2 == 0:
    print(x[len(x)//2-1]+x[len(x)//2])
else:
    print(x[len(x)//2])
print(input())