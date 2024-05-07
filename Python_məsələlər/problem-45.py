'''
45. 1-dən n-1-ə qədər cüt ədədlərin kvadratlarını hesablayan proqram
qurun.
'''
n = int(input())
for i in range(1,n):
    if i%2==0:
        print(i**2)