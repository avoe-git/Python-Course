# a və b ədədlərinin ƏKOB-unu çap edən proqram
a = int(input("Birinci ədəd daxil edin: "))
b = int(input("İkinci ədəd daxil edin: "))

while a != b:
    if a > b:
        a -= b
    else:
        b -= a

ekob = (a * b) // a

print(ekob)
