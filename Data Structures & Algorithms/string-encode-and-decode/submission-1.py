class Solution:

    def encode(self, strs: List[str]) -> str:
        code = []
        for i in strs:
            code.append(str(len(i)))
            code.append('#')
            code.append(i)
        return "".join(code)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            tmp = int(s[i:j])
            word = s[j+1:j+1+tmp]
            ans.append(word)
            i = tmp+1+j
        return ans