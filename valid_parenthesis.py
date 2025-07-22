class Solution:
    # Approach-1 with extra space (Map and Stack)
    def isValid(self, s: str) -> bool:
            stack = []
            if len(s) <= 1:
                return False
            m = {'(' : ')',
                '[' : ']',
                '{' : '}' }
            for i in range(len(s)):
                if s[i] in m:
                    stack.append(s[i])
                elif stack and m[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
            if stack:
                return False
            return True
    # Approach - 2 without extra space for Map
    # def isValid(s: str) -> bool:
    #     st = []
    #     for it in s:
    #         if it == '(' or it == '{' or it == '[':
    #             st.append(it)
    #         else:
    #             if len(st) == 0:
    #                 return False
    #             ch = st[-1]
    #             st.pop()
    #             if (it == ')' and ch == '(') or (it == ']' and ch == '[') or (it == '}' and ch == '{'):
    #                 continue
    #             else:
    #                 return False
    #     return len(st) == 0

            


# --- Direct Function Calls for Testing ---
if __name__ == "__main__":
    sol = Solution()
    s = "()[{}()]"
    print(sol.isValid(s))