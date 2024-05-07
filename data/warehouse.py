def minVehicles(w, l):
    sw = sorted(filter(lambda x:x!=0,w),reverse=True)
    left, right = 0, len(sw) - 1
    v = 0
    
    while left <= right:
        if sw[left] + sw[right] <= l:
            right -= 1
        left += 1
        v += 1
    return v
try:
    raw_input = input
except NameError:
    pass

weights = list(map(int, raw_input().split()))
limit = int(raw_input())
r= minVehicles(weights, limit)
print(r, end="")