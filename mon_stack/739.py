temperatures = [73,74,75,71,69,72,76,73]
# l = len(temperatures)
# res = l * [0]
# stack = []
# for key, val in enumerate(temperatures):
#     while stack and val > temperatures[stack[-1]]:
#         res[stack[-1]] = key - stack[-1]
#         stack.pop()
#     stack.append(key)
# print(res)

res = [0] * len(temperatures)
stack = []
for key, val in enumerate(temperatures):
    while stack and val > temperatures[stack[-1]]:
        res[stack[-1]] = key - stack[-1]
        stack.pop()

    stack.append(key)
print(res)