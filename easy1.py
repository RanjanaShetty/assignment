s=input()
s=s.split()
print(len(s[-1]))


#OR

s=input()
count=0
for i in range(-1,-len(s)-1,-1):
    if s[i]==' ' and count==0:
        continue
    if s[i]!=' ':
        count+=1
    elif s[i]==' ':
        break
print(count)
