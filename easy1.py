st=input()
count=0
for i in range(-1,-len(st)-1,-1):
    if st[i]==' ' and count==0:
        continue
    if st[i]!=' ':
        count+=1
    elif st[i]==' ':
        break
print(count)
