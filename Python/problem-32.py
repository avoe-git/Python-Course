'''
32. Üçbucağın tərəflərinin verilmiş qiymətlərinə görə onun perimetrini
hesablayan funksiya yazın.
'''
d = list(map(int,input().split(' ')))

def perimeter(c):
    c=c[0]+c[1]+c[2]
    print('Perimetr:',c)

perimeter(d)