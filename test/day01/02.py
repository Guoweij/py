class Solution:
    def editDistance(self, word1, word2):
        word1 = word1
        word2 = word2
        word2 = word1.replace('h', 'r')
        return word1, word2


word1 = "horse"
word2 = "ros"
str1 = Solution()
print(str1.editDistance(word1, word2))
