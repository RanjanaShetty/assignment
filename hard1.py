#window_size
k=int(input())

#input array
n=int(input())
nums=[int(input()) for x in range(n)]

left_index=0
right_index=k
window_elements=[]
maxround=0
maxfinal=0
for i in range(n-k+1):
    for j in range(left_index,right_index,):
        window_elements.append(nums[j])
    maxround=max(window_elements)
    maxfinal=max(maxfinal,maxround)
    left_index+=1
    right_index+=1
    window_elements=[]
    print(maxfinal)
