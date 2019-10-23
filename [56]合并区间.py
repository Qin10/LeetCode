# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1: 
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
#
# 示例 2: 
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# Related Topics 排序 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        size = len(intervals)
        res = []
        queue = []
        if size <= 1:
            return intervals
        intervals.sort()
        for i in intervals:
            queue.append(i)
            if len(queue) == 2:
                if queue[0][1] >= queue[1][0]:
                    queue = [[queue[0][0], max(queue[0][1], queue[1][1])]]
                else:
                    res.append(queue[0])
                    queue.pop(0)
        res.append(queue[0])
        queue.pop(0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
