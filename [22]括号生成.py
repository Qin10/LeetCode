# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为： 
#
# [
#  "((()))",
#  "(()())",
#  "(())()",
#  "()(())",
#  "()()()"
# ]
# 
# Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
import copy


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left_count = [0]
        count_temp = []
        temp = [""]
        result = []
        for i in range(n * 2):
            result = []
            count_temp = []
            for index, j in enumerate(temp):
                if left_count[index] == 0:
                    result.append(j + "(")
                    count_temp.append(left_count[index] + 1)
                elif j.count("(") < n:
                    result.append(j + "(")
                    count_temp.append(left_count[index] + 1)
                    result.append(j + ")")
                    count_temp.append(left_count[index] - 1)
                else:
                    result.append(j + ")")
                    count_temp.append(left_count[index] - 1)
            temp = copy.deepcopy(result)
            left_count = copy.deepcopy(count_temp)
        return result
# leetcode submit region end(Prohibit modification and deletion)
