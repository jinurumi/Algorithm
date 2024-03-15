str = input()
ans = ''
for i in range(len(str)):
    if str[i] == str[i].upper():
        ans+=str[i].lower()
    elif str[i] == str[i].lower():
        ans+=str[i].upper()
print(ans)