gain = [-4, -3, -2, -1, 4, 3, 2]
res = [0] * (len(gain) + 1)
tmp = 0
for i in range(1, len(gain)+1):
    tmp += gain[i-1]
    res[i] = tmp
print(res)