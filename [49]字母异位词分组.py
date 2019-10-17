# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例: 
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
# ]
#
# 说明： 
#
# 
# 所有输入均为小写字母。 
# 不考虑答案输出的顺序。 
# 
# Related Topics 哈希表 字符串



# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        lst = []
        res = []
        temp = []
        for i in range(len(strs)):
            dic = {}
            for s in strs[i]:
                if s not in dic:
                    dic[s] = 1
                else:
                    dic[s] += 1
            lst.append(dic)
            if lst[i] not in temp:
                temp.append(lst[i])
                res.append([strs[i]])
            else:
                res[temp.index(lst[i])].append(strs[i])
        return res

# leetcode submit region end(Prohibit modification and deletion)
