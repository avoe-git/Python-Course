a="1abcxtkl207o57bstr"
numbers=['1','2','3','4','5','6','7','8','9','0']
s=0
for i in range(len(a)):
    if a[i] in numbers:
        s=s+int(a[i])
print(s)