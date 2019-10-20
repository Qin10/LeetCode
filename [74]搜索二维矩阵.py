# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
# 
# 每行中的整数从左到右按升序排列。 
# 每行的第一个整数大于前一行的最后一个整数。 
# 
#
# 示例 1: 
#
# 输入:
# matrix = [
#  [1,   3,  5,  7],
#  [10, 11, 16, 20],
#  [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
# 
#
# 示例 2: 
#
# 输入:
# matrix = [
#  [1,   3,  5,  7],
#  [10, 11, 16, 20],
#  [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
# Related Topics 数组 二分查找



# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        m_left = 0
        m_right = m - 1
        n_left = 0
        n_right = n - 1
        while m_right > m_left:
            m_mid = (m_right + m_left) // 2
            if matrix[m_mid][-1] == target:
                return True
            elif matrix[m_mid][-1] > target:
                if matrix[m_mid][0] > target:
                    m_right = m_mid - 1
                else:
                    m_left, m_right = m_mid, m_mid
            else:
                if matrix[m_mid][0] < target:
                    m_left = m_mid + 1
                else:
                    m_left, m_right = m_mid, m_mid
        while n_right >= n_left:
            n_mid = (n_right + n_left) // 2
            if matrix[m_left][n_mid] == target:
                return True
            elif matrix[m_left][n_mid] > target:
                n_right = n_mid - 1
            else:
                n_left = n_mid + 1
        return False

# leetcode submit region end(Prohibit modification and deletion)
