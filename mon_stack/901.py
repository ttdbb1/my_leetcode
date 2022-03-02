# class StockSpanner:
#
#     def __init__(self):
#         self.stack = []
#
#     def next(self, price):
#         w = 1
#         while self.stack and price >= self.stack[-1][0]:
#             w += self.stack[-1][1]
#             self.stack.pop()
#         self.stack.append([price, w])
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):
        w = 1
        while self.stack and price > self.stack[-1][0]:
            w += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, w])
        return w