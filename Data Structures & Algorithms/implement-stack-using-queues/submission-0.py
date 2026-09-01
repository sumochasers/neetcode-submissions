class MyStack:

    def __init__(self):
        self.nums_arr = []

    def push(self, x: int) -> None:
        self.nums_arr.append(x)

    def pop(self) -> int:
        return self.nums_arr.pop()

    def top(self) -> int:
        return self.nums_arr[-1]

    def empty(self) -> bool:
        return len(self.nums_arr) == 0
         


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()