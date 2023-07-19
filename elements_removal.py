a = list(map(int,input("Enter the array elements : ").split()))
def element_rem(a):
    n = len(a)
    cost=0
    for i in range(n):
        cost =cost+ (a[i]*(i+1))
    return cost
print(element_rem(sorted(a,reverse= True)))

