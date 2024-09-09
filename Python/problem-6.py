'''
6. Üçbucaq bərabərsizliyini ödəyən proqram tərtib edin. (Üçbucağın hər
bir tərəfinin uzunluğu digər iki tərəfinin uzunluqları cəmindən kiçikdir?)
'''

a = int(input('1-ci teref:  '))
b = int(input('2-ci teref:  '))
c = int(input('3-cu teref:  '))

if a < b+c and b < a+c and c < a+b:
    print('Duzgun ucbucaqdir!')
else:
    print('Ucbucaq duzgun deyildir!')