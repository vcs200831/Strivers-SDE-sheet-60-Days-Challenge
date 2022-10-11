class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n_i = n_j = float('inf')
        for n in nums:
            if n <= n_i:
                n_i = n
            elif n <= n_j:
                n_j = n
            else:
                return True
        return False