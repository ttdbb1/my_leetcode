from collections import Counter
"""单调递减栈
    stack中的元素作为结果
    返回结果的字典序最小---从小到大的单调栈
    消除重复数字，循环内部加个判断continue即可
    [abcd]
"""
s = "cbacdcbc"
# news = Counter(s)
# stack = []
# for key, val in enumerate(s):
#     if val not in stack:
#         while stack and val < stack[-1] and news[stack[-1]] > 1:
#             stack.pop()
#         stack.append(val)
# print(stack)

new_dic = Counter(s)
stack = []
for key, val in enumerate(s):
    if val not in stack:
        while stack and new_dic[stack[-1]] > 1 and val < stack[-1]:
            stack.pop()
        stack.append(val)
print(stack)