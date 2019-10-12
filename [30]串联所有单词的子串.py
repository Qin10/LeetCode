# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
#
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。 
#
# 
#
# 示例 1： 
#
# 输入：
#  s = "barfoothefoobarman",
#  words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
# 
#
# 示例 2： 
#
# 输入：
#  s = "wordgoodgoodgoodbestword",
#  words = ["word","good","best","word"]
# 输出：[]
# 
# Related Topics 哈希表 双指针 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        length = len(words)
        length_word = len(words[0])
        if len(s) < length * length_word:
            return []
        words.sort()
        result = []
        for i in range(len(s) - length * length_word + 1):
            temp_str = s[i:length * length_word + i]
            temp_words = []
            for j in range(length):
                temp_words.append(temp_str[length_word * j:length_word * (j + 1)])
            temp_words.sort()
            # print(temp_words)
            if temp_words == words:
                result.append(i)
        return result
# leetcode submit region end(Prohibit modification and deletion)
