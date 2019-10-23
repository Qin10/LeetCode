# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 
#
# 上图为 8 皇后问题的一种解法。 
#
# 给定一个整数 n，返回 n 皇后不同的解决方案的数量。 
#
# 示例: 
#
# 输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 
# Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        def backtrack(cuur=[], res=0):
            i = len(cuur)
            if i == n:
                res += 1
                return res
            for j in range(n):
                if can_put(i, j) and j not in cuur:
                    cuur.append(j)
                    sum_list[i + j] = False
                    diff_list[i - j + n - 1] = False
                    res = backtrack(cuur, res)
                    cuur.pop()
                    sum_list[i + j] = True
                    diff_list[i - j + n - 1] = True
            return res

        def can_put(x, y):
            if not sum_list[x + y] or not diff_list[x - y + n - 1]:
                return False
            return True

        sum_list = [True for i in range(2 * n - 1)]
        diff_list = [True for i in range(2 * n - 1)]
        return backtrack()
# leetcode submit region end(Prohibit modification and deletion)
