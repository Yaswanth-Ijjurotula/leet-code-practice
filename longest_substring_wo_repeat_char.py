class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # BF-Approach - (O(N2)
        # hashset = set()
        # max_l = 0
        # for i in range(len(s)):
        #     cnt = 1
        #     hashset.add(s[i])
        #     for j in range(i+1,len(s)):
        #         if s[j] not in hashset:
        #             hashset.add(s[j])
        #             cnt += 1
        #         else:
        #             hashset.clear()
        #             break
        #     max_l = max(cnt,max_l)
        # return max_l
        #Optimal Approach - 1(O(2N))
        # st = set()
        # if len(s)==0:
        #     return 0
        # l = 0
        # r = 0
        # max_l = 0
        # while(r<len(s)):
        #     if s[r] not in st:
        #         st.add(s[r])
        #         max_l = max(max_l,r-l+1)
        #         r += 1
        #     else:
        #         while(l<r and s[r] in st):
        #             st.remove(s[l])
        #             l+=1
        # return max_l
        #Optimal Approach-2(O(N))
        map = {}
        if len(s)==0:
            return 0
        l = 0
        r = 0
        max_l = 0
        while(r < len(s)):
            if s[r] in map and map[s[r]] >= l:
                    l = map[s[r]] + 1
            map[s[r]] = r
            max_l = max(max_l,r-l+1)
            r += 1    
        return max_l
                


def main():
    sol = Solution()

    # Test cases
    s1 = "abcabcbb"
    print(f"Input: \"{s1}\", Output: {sol.lengthOfLongestSubstring(s1)}") # Expected: 3 (abc)

    s2 = "bbbbb"
    print(f"Input: \"{s2}\", Output: {sol.lengthOfLongestSubstring(s2)}") # Expected: 1 (b)

    s3 = "pwwkew"
    print(f"Input: \"{s3}\", Output: {sol.lengthOfLongestSubstring(s3)}") # Expected: 3 (wke)

    s4 = ""
    print(f"Input: \"{s4}\", Output: {sol.lengthOfLongestSubstring(s4)}") # Expected: 0

    s5 = " "
    print(f"Input: \"{s5}\", Output: {sol.lengthOfLongestSubstring(s5)}") # Expected: 1 ( )

    s6 = "au"
    print(f"Input: \"{s6}\", Output: {sol.lengthOfLongestSubstring(s6)}") # Expected: 2 (au)

    s7 = "dvdf"
    print(f"Input: \"{s7}\", Output: {sol.lengthOfLongestSubstring(s7)}") # Expected: 3 (vdf)

    s8 = "aab"
    print(f"Input: \"{s8}\", Output: {sol.lengthOfLongestSubstring(s8)}") # Expected: 2 ()

    s9 = "tmmzuxt"
    print(f"Input: \"{s9}\", Output: {sol.lengthOfLongestSubstring(s9)}")

if __name__ == "__main__":
    main()