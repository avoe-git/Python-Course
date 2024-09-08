'''
4. Daxil edilmiş sətridə sözlər arasında birdən çox boşluqları silən
proqram tərtib edin.
'''

a = input()
new_str =''
for i in range(len(a)): 
    if a[i] == ' ' and a[i+1] == ' ':
        new_str = new_str + ''
    else: 
        new_str = new_str + a[i]

print(new_str)