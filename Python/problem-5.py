'''
5. Tekstil şirkətinin işçiləri həftənin bütün günləri ərzində sifariş edilən
məhsulların sayını özündə saxlayan ədədlərdən ibarət siyahı tərtib
edirlər. Son bir həftə ərzində sifariş edilən malları siyahıya daxil edən
proqram tərtib edin.
'''

hesabat=[]
indicator = input('Mehsulu daxil edin. Stoplamaq ucun "no" daxil et:   ')
while indicator != 'no':
    hesabat.append(indicator)
    if indicator == 'no':
        break
    else:
        indicator = input('Mehsulu daxil edin. Stoplamaq ucun "no" daxil et:   ')
print(', '.join(hesabat))