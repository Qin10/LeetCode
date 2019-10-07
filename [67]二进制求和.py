# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。 
#
# 示例 1: 
#
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2: 
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# Related Topics 数学 字符串



# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a
        n = len(a)
        b = '0' * (n - len(b)) + b  # 补齐 b 不足的位为 0
        result = ''
        summ = 0  # 进位值
        for i in range(n):
            a_1 = int(a[-i - 1])
            b_1 = int(b[-i - 1])
            result = str((a_1 + b_1 + summ) % 2) + result  # 当前位数相加模 2 ，链接更小位数的值
            summ = (a_1 + b_1 + summ) // 2  # 当前位数之和整除二，得到下一位运算的进位值

        if summ == 1:  # 判断最高位是否需要进位
            result = '1' + result
        return result

# leetcode submit region end(Prohibit modification and deletion)
