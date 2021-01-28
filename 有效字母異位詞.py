# 我的解法 時:O(N) 空:O(N)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        for i, j in zip(s, t):
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
            if j not in dict2:
                dict2[j] = 1
            else:
                dict2[j] += 1

        return dict1 == dict2
