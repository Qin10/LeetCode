#给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
#
# 示例 1： 
#
# 输入: "babad"
#输出: "bab"
#注意: "aba" 也是一个有效答案。
# 
#
# 示例 2： 
#
# 输入: "cbbd"
#输出: "bb"
# 
# Related Topics 字符串 动态规划



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        s2 = s[::-1]
        while n > 0:
            for i in range(len(s) - n + 1):
                if s[i: i + n] == s2[len(s) - i - n: len(s) - i]:
                    return s[i: i + n]
            n -= 1
        return ""
#leetcode submit region end(Prohibit modification and deletion)
