class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = s[0]
        for center_i in range(len(s) - 1):
            if s[center_i] == s[center_i + 1]:
                left_i = center_i
                right_i = center_i + 1
                while left_i >= 0 and right_i < len(s):
                    if s[left_i] != s[right_i]:
                        break

                    palindrome = s[left_i:right_i + 1]
                    if len(palindrome) > len(max_palindrome):
                        max_palindrome = palindrome
                    
                    left_i -= 1
                    right_i += 1
            
            left_i = center_i
            right_i = center_i
            while left_i >= 0 and right_i < len(s):
                if s[left_i] != s[right_i]:
                    break

                palindrome = s[left_i:right_i + 1]
                if len(palindrome) > len(max_palindrome):
                    max_palindrome = palindrome
                
                left_i -= 1
                right_i += 1

        return max_palindrome



"0 1 2 3 4 5 6 7 8 9"
" b a a b a a b a a"
print(Solution().longestPalindrome('baabacababb'))
