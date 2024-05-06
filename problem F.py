a = input()
x = 0
f= []

for i in a:
    if i == 'b':
        x = x+1
    else: 
        f.append(x)
        x=0
print(max(f))