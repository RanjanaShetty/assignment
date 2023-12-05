n=int(input())
arr=[int(input()) for x in range(n)]
arr1=[]
for i in arr:
    if arr.count(i)>n/3 and i not in arr1:
        arr1.append(i)
print(arr1)
