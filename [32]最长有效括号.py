# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
# 示例 1: 
#
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 
#
# 示例 2: 
#
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 
# Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip(")")
        s = s.rstrip("(")
        stack = []
        max_count = 0
        count = []
        sum_count = 0
        for i in s:
            if i == "(":
                stack.append(i)
                count.append(0)
            else:
                if len(stack) >= 1 and stack[-1] == "(":
                    stack.pop()
                    for k in range(-1, -len(count) - 1, -1):
                        if count[k] == 0:
                            count[k] = 2
                            break
                else:
                    count.append(0)
                    stack.append(")")
        for j in count:
            if j != 0:
                sum_count += 2
            else:
                max_count = max(sum_count, max_count)
                sum_count = 0
        return max(sum_count, max_count)
# leetcode submit region end(Prohibit modification and deletion)
