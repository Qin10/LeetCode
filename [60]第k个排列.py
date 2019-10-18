# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下： 
#
# 
# "123" 
# "132" 
# "213" 
# "231" 
# "312" 
# "321" 
# 
#
# 给定 n 和 k，返回第 k 个排列。 
#
# 说明： 
#
# 
# 给定 n 的范围是 [1, 9]。 
# 给定 k 的范围是[1, n!]。 
# 
#
# 示例 1: 
#
# 输入: n = 3, k = 3
# 输出: "213"
# 
#
# 示例 2: 
#
# 输入: n = 4, k = 9
# 输出: "2314"
# 
# Related Topics 数学 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        temp = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        a = (k - 1) // temp[n - 1]
        b = (k - 1) % temp[n - 1]
        res = ""
        lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        while a >= 0 and n > 1:
            res += lst[a]
            lst.pop(a)
            k = b
            n = n - 1
            a = k // temp[n - 1]
            b = k % temp[n - 1]
        return res + lst[a]
# leetcode submit region end(Prohibit modification and deletion)
