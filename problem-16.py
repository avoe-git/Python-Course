'''
16. Sıra nömrəsinə görə Fibonaççi ədədini qaytaran proqram tərtib edin. 
Fibonaççi sırası - ikincidən başlayaraq hər bir hədd özündən əvvəlki iki həddin cəminə bərabərdir. 
(1, 1, 2, 3, 5, 8, 13, 21,...)
'''

s = int(input())
a=0
f = 1
f2 = 1
while a != s:
    f=f2+f
    f2=f+f2
    a+=1
print(f)