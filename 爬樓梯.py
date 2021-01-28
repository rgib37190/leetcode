#動態規劃的解法 時:O(N), 空:O(N)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp_table = [0 for _ in range(n+1)]
        for i in range(n+1):
            if i == 0 or i == 1:
                dp_table[i] = 1
            else:
                dp_table[i] = dp_table[i-1] + dp_table[i-2]
        return dp_table[n]
 
# 動態規劃加滾動 時:O(N), 空:O(1)
# 因為這題的狀態只根據前面兩個，所以可以這麼做
class Solution:
    def climbStairs(self, n: int) -> int:
        p, q, r = 0, 0, 1
        for i in range(n):
            p = q
            q = r
            r = p + q
        return r
