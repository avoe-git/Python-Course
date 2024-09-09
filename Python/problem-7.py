'''
7. 1!+2!+3!+4!+...+n! cəmini hesablayan proqram tərtib edin. n natural
ədəddir.
'''

a = int(input())
f = 1
l = 0
for i in range(1, a+1):
    for x in range(1, i+1):
        f = f*x
    l=l+f
    f=1
print(l)
