import math

class Solution:
    def divFloorCeil(self,a,b):
        floor_val=math.floor(a/b)

        ceil_val=math.ceil(a/b)

        res=[floor_val,ceil_val]

        print(res)