class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num, a, b = len(nums), sum(nums), sum(set(nums))
		
        s = num*(num+1)//2
        
        return [a-b, s-b]