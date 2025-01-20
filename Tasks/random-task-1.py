cumle=input()
cumle_list=cumle.split(' ')
leng=0
for i in cumle_list:
    if len(i)>leng:
        leng=len(i)
        soz=cumle_list[cumle_list.index(i)]
print(leng)
print(soz)