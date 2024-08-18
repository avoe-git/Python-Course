'''
3. color = ['aqua 0 255 255', 'black 0 0 0', 'blue 0 0 255', 'fuchsia 255 0
255', 'gray 128 128 128', 'green 0 128 0', 'lime 0 255 0', 'red 255 0 0',
'white 255 255 255', 'yellow 255 255 0']
Proqram eyni anda rəngi və boşluq vasitəsilə onun RGB formatında
nömrəsini saxlayan verilənlər bazası ilə işləyir.
255 ədədinin ən azı bir dəfə rast gəlindiyi bütün rəngləri və bu rənglərin
sayını ekranda əks etdirin.

Çıxışda alınmalıdır:
aqua 0 255 255
blue 0 0 255
fuchsia 255 0 255
lime 0 255 0
red 255 0 0
white 255 255 255
yellow 255 255 0
Cəmi 7 belə element var.
'''

color = ['aqua 0 255 255', 'black 0 0 0', 'blue 0 0 255', 'fuchsia 255 0 255', 'gray 128 128 128', 'green 0 128 0', 'lime 0 255 0', 'red 255 0 0','white 255 255 255', 'yellow 255 255 0']
a= ''
x=0
for i in range(len(color)):
    if '255' in color[i]:
        a += color[i] + '\n'
        x+=1
print(a + 'Cəmi', x ,'belə element var.')