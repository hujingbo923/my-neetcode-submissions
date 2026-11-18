class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minstack.append(val)
            return
        if val < self.minstack[-1]:
            self.minstack.append(val)
            self.stack.append(val)
        else:
             self.stack.append(val)
             self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
    #辅助最小栈
    #操作之前，数据结构是什么状态？
    #操作之后，数据结构应该变成什么状态？
    #如果删除了某个元素，之前的信息是否还需要保留？
    #如果我只用一个min存储，我的getmin不会改变这个变量，所以需要维护一个辅助栈，当前元素是stack中的min