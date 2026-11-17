class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i]=='{' or s[i]=='[' or s[i]=='(':
                stack.append(s[i])

            if s[i]=='}':
                if stack!=[]:#务必判断stack是不是空
                    tmp=stack.pop()
                    if tmp =='{':
                        continue
                    else:
                        return False
                else:
                    return False
            if s[i]==']':
                if stack!=[]:
                    tmp=stack.pop()
                    if tmp =='[':
                        continue
                    else:
                        return False
                else:
                    return False
            if s[i]==')':
                if stack!=[]:
                    tmp=stack.pop()
                    if tmp =='(':
                        continue
                    else:
                        return False
                else:
                    return False
        if stack ==[]:
            return True
        else:
            return False
            
                