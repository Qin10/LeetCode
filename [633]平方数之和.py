#给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。 
#
# 示例1: 
#
# 
#输入: 5
#输出: True
#解释: 1 * 1 + 2 * 2 = 5
# 
#
# 
#
# 示例2: 
#
# 
#输入: 3
#输出: False
# 
# Related Topics 数学



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        left = 0
        right = int(math.sqrt(c))
        while left <= right:
            ss = left * left + right * right
            if ss == c:
                return True
            elif ss > c:
                right -= 1
            else:
                left += 1
        return False
#leetcode submit region end(Prohibit modification and deletion)
