class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if (len(x) % 2) == 0:
            half = int(len(x) / 2)
            if x[half:] == x[:-half][::-1]:
                return True
            else:
                return False
        else:
            half = int(len(x) / 2)
            if x[half+1:] == x[:half]:
                return True
            else:
                return False