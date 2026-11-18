class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for i in tokens:
            if i != '+' and i != '-' and i != '*'and i != '/':
                stack.append(int(i))
            else:
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                if i == '+':
                    stack.append(temp1+temp2)
                if i == '-':
                    stack.append(temp2-temp1)
                if i == '*':
                    stack.append(temp1*temp2)
                if i == '/':
                    stack.append(int(temp2/temp1))
        return stack.pop()