# My version speed too slow
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
            if x > 2**31 -1:
                return 0
        else:
            x = -x # difference
            x = str(x)
            x = x[::-1]
            x = -int(x)
            if x < -2**31:
                return 0
        return x


# other version

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
            if x > 2**31 -1:
                return 0
        else:
            x = str(x)
            x = x[1:][::-1]
            x = -int(x)
            if x < -2**31:
                return 0
        return x