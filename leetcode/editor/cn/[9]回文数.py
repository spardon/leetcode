# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。 
# 
#  示例 1: 
# 
#  输入: 121
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#  
# 
#  示例 3: 
# 
#  输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#  
# 
#  进阶: 
# 
#  你能不将整数转为字符串来解决这个问题吗？ 
#  Related Topics 数学 
#  👍 1172 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        sx = str(x)
        # return True if 0 <= x < 10 or sum([int(sx[i] == sx[-i-1]) for i in range(len(sx) // 2)]) == len(sx) // 2 else False

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(-12))
# leetcode submit region end(Prohibit modification and deletion)
