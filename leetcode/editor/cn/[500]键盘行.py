# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。 
# 
#  
# 
#  
# 
#  
# 
#  示例： 
# 
#  输入: ["Hello", "Alaska", "Dad", "Peace"]
# 输出: ["Alaska", "Dad"]
#  
# 
#  
# 
#  注意： 
# 
#  
#  你可以重复使用键盘上同一字符。 
#  你可以假设输入的字符串将只包含字母。 
#  Related Topics 哈希表 
#  👍 103 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findWords(self, words):
        keyboardRows = [
            {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
            {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
            {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        ]
        res = []
        for word in words:
            wordSet = set(word.lower())
            for rowSet in keyboardRows:
                if wordSet <= rowSet:
                    res.append(word)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findWords(["asdfghjkl","qwertyuiop","zxcvbnm"]))
# leetcode submit region end(Prohibit modification and deletion)
