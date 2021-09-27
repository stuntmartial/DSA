#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0 or len(s)==1:
            return len(s)

        windStart=0;windEnd=0;windHash={s[0]:0}
        currLen=1;maxLen=1

        for index in range(1,len(s)):
            ch=s[index]

            if ch not in windHash.keys():
                windEnd+=1;currLen+=1;maxLen=max(maxLen,currLen)
                windHash[ch]=index
            else:
                pos=windHash[ch]
                chars=[i for i in s[windStart:pos+1]]
                popFromHash(windHash, chars)

                windStart=pos+1;windEnd=index
                currLen=windEnd-windStart+1
                maxLen=max(maxLen,currLen)
                windHash[ch]=index
                
        return maxLen

def popFromHash(ht,keys):
    for key in keys:
        ht.pop(key)


# @lc code=end

