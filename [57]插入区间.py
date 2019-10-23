# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。 
#
# 示例 1: 
#
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
# 
#
# 示例 2: 
#
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
# 
# Related Topics 排序 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        size = len(intervals)
        if size == 0:
            return [newInterval]
        found = False
        i = 0
        while i < size:
            if intervals[i][0] > newInterval[1] and not found:
                intervals.insert(0, newInterval)
                break
            elif intervals[i][1] >= newInterval[0] and not found:
                intervals[i] = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                found = True
                i += 1
                continue
            elif i == size - 1 and not found:
                intervals.append(newInterval)
                break
            elif intervals[i][1] < newInterval[0] and intervals[i + 1][0] > newInterval[1] and not found:
                intervals.insert(i + 1, newInterval)
                break
            if found and (intervals[i - 1][1] >= intervals[i][0] or (
                    intervals[i - 1][1] <= intervals[i][1] and intervals[i - 1][1] >= intervals[i][0])):
                intervals[i - 1][1] = max(intervals[i][1], intervals[i - 1][1])
                intervals.pop(i)
                size -= 1
                continue
            elif found and intervals[i - 1][1] > intervals[i][0]:
                break
            i += 1
        return intervals
# leetcode submit region end(Prohibit modification and deletion)
