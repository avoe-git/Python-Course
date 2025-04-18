k = int(input('Neçə ədəd daxil ediləcək: '))
b = []
for i in range(k):
    a = input()
    b.append(int(a))
k = 1
j = 1
x = False
for i in b: 
    if k != j:
        x = False
        print('deyil')
    if not(b[(b.index(i))+1] <= len(b)-1):
        j = b[(b.index(i))+1] - i
        k = j
        x = True
    else:
        
        break
if x == True:
    print('bəli')
    