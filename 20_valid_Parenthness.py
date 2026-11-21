class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0 or len(s) == 1:
            return False

        open = ['(','{','[']
        close = [')','}',']']

        pairs = [(open[0],close[0]),(open[1],close[1]),(open[2],close[2])]

        stack = []
        for ch in s:
            if ch in open:
                stack.append(ch)
            if ch in close:
                if (len(stack) != 0):
                    opench = stack.pop()
                else:
                    return False
                if (opench, ch) not in pairs:
                    return False
        if(len(stack) !=0):
            return False
        
        return True


if __name__ == "__main__":

    sol = Solution()

    s = "{("

    print(sol.isValid(s))