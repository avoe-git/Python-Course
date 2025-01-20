ascii=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a = input('Dekodlaşdırılmış sətir daxil edin: ')
k = int(input('Kod əmsalınızı daxil edin: '))
result = []
for i in a:
    if i != ' ':
        if i == i.lower():
            result.append(ascii[(ascii.index(i)+k)%len(ascii)])
        else:
            i = i.lower()
            result.append(ascii[(ascii.index(i)+k)%len(ascii)].upper())
    else:
        result.append(' ')
print('Kodlaşdırılmış nəticə: '+''.join(result))