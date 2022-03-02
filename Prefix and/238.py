s = [1, 2, 3, 4]
# l = len(s)
# data = [0] * l
# data[0] = 1
# for i in range(1, l):
#     data[i] = s[i-1] * data[i-1]
#
# R = 1
# for j in range(l-1, -1, -1):
#     data[j] = R * data[j]
#     R *= s[j]
# print(data)

a = [1] * len(s)
for i in range(1, len(s)):
    a[i] = s[i-1] * a[i-1]

b = [1] * len(s)

for j in range(len(s)-2, -1, -1):
    b[j] = s[j+1] * b[j+1]

for k in range(0, len(s)):
    a[k] = a[k] * b[k]
print(a)