# http://yucoding.blogspot.com/2016/12/leetcode-question-h-index.html

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        ssum = 0
        sz = len(citations)
        mp = [0]*(sz+1)

        for ci in citations:
            mp[min(sz,ci)] +=1

        for i in range(sz,-1,-1):
            ssum += mp[i]
            if ssum>=i:
                return i

        return 0
