"""
单调递增栈
num1 在num2中下一个比他大的数字
[5,4,3,6]
对于 for i in：
        if
        else
用列表迭代式来替换
"""
num1 = [4, 1, 2]
num2 = [1, 3, 4, 2]
# stack = []
# dic= {}
# for key, val in enumerate(num2):
#     while stack and val > stack[-1]:
#         dic[stack[-1]] = val
#         stack.pop()
#     stack.append(val)
# print([dic[num] if dic.get(num) else -1 for num in num1])

stack = []
dic = {}
for key, val in enumerate(num2):
    while stack and val > stack[-1]:
        dic[stack[-1]] = val
        stack.pop()
    stack.append(val)
print([dic[i] if dic.get(i) else -1 for i in num1])