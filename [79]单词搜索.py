#给定一个二维网格和一个单词，找出该单词是否存在于网格中。 
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
#
# 示例: 
#
# board =
#[
#  ['A','B','C','E'],
#  ['S','F','C','S'],
#  ['A','D','E','E']
#]
#
#给定 word = "ABCCED", 返回 true.
#给定 word = "SEE", 返回 true.
#给定 word = "ABCB", 返回 false. 
# Related Topics 数组 回溯算法



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])

        def helper(i, j, k, visited):
            # print(i,j, k,visited)
            if k == len(word):
                return True
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j) not in visited \
                        and board[tmp_i][tmp_j] == word[k]:
                    visited.add((tmp_i, tmp_j))
                    if helper(tmp_i, tmp_j, k + 1, visited):
                        return True
                    visited.remove((tmp_i, tmp_j))
            return False

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and helper(i, j, 1, {(i, j)}):
                    return True
        return False
#leetcode submit region end(Prohibit modification and deletion)
