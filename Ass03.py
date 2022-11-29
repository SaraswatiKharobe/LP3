#fraction knapsack problem
def fra(W,arr):
    sum=0
    arr.sort(key=lambda x:x[0]/x[1],reverse=True)
    for i in range(len(arr)):
        if arr[i][1]<=W:
            W-=arr[i][1]
            sum+=arr[i][0]
        
        elif arr[i][1]>W:
            sum+=arr[i][0]*W/arr[i][1]
            break
    return sum

print(fra(50,[[60,10],[100,20],[120,30]]))