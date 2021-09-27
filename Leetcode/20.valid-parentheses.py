#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stk=list()
        openBrackets=['(','{','[']
        closeBrackets=[')','}',']']
        
        for ch in s:
            if ch in openBrackets:
                stk.append(ch)
            else:
                if len(stk)==0:
                    return False
                    
                stkTop=stk[-1]
                for i in range(len(openBrackets)):
                    if openBrackets[i]==stkTop:
                        break

                openBracketIndex=i
                for i in range(len(closeBrackets)):
                    if closeBrackets[i]==ch:
                        break
                
                closeBracketIndex=i

                if openBracketIndex==closeBracketIndex:
                    stk.pop(-1)
                    continue
                else:
                    return False
        if len(stk)==0:
            return True
        else:
            return False
# @lc code=end

