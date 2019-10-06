# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足： 
#
# 
# 左括号必须用相同类型的右括号闭合。 
# 左括号必须以正确的顺序闭合。 
# 
#
# 注意空字符串可被认为是有效字符串。 
#
# 示例 1: 
#
# 输入: "()"
# 输出: true
# 
#
# 示例 2: 
#
# 输入: "()[]{}"
# 输出: true
# 
#
# 示例 3: 
#
# 输入: "(]"
# 输出: false
# 
#
# 示例 4: 
#
# 输入: "([)]"
# 输出: false
# 
#
# 示例 5: 
#
# 输入: "{[]}"
# 输出: true
# Related Topics 栈 字符串



# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        brackets = ["(", ")", "[", "]", "{", "}"]
        stack = []
        for i in s:
            stack.append(i)
            index = brackets.index(i)
            if index % 2 == 1:
                if len(stack) == 1:
                    return False
                if stack[-2] != brackets[index - 1]:
                    return False
                else:
                    stack = stack[:-2]
        return stack == []

    # 用map代替数组，减少查找时间
    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack

# leetcode submit region end(Prohibit modification and deletion)
