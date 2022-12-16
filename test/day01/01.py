#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param userLogId string字符串 用户携带的logids
# @param pmLogId string字符串 产品经理设置的实验logid
# @return bool布尔型
#
class Solution:
    def ContainsAny(self, userLogId, pmLogId):
        userLogId = userLogId
        pmLogId = pmLogId
        if userLogId == pmLogId:
            return bool()
        else:
            return bool()


test = Solution()
print(test.ContainsAny("2021,2031", "2041"))
print(test.ContainsAny("2021,2031", "2021"))
print(test.ContainsAny("2021,2031", "2021,2041"))
