class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_finish(x):
            hours = 0
            for i in piles:
                hours+= (i + x - 1)//x
            return True if hours <= h else False
        
        slowest = 1
        fastest = max (piles)

        eatingSpeed = fastest
        while slowest <= fastest:
            mid = slowest + (fastest - slowest)//2
            if can_finish(mid):
                fastest = mid - 1
                eatingSpeed = mid
            else:
                slowest = mid + 1
        return eatingSpeed
