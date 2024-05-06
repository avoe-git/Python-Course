'''
35. Latın əlifbası ilə yazılmış sətirdə neçə hərfin böyük, neçəsinin isə
kiçik hərflərlə yazıldığını müəyyənləşdirin.
'''
capitals=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a = input()
cap=0
let=0
for i in a:
    if i in capitals:
        cap +=1
    elif i in letters:
        let+=1
print(cap,'BOYUK',let,'kicik')