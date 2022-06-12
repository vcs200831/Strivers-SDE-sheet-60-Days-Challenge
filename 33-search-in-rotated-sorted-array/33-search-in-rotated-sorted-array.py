class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st = 0
        end = len(nums) - 1
        
        while(st <= end):
            mid = st + (end - st) // 2
        
            if(nums[mid] == target):
                return mid
        
            elif(nums[mid] >= nums[st]):
                if(nums[st] <= target and target <= nums[mid]):
                    end = mid - 1
                else :
                    st = mid + 1
            
            else :
                if(nums[end] >= target and target >= nums[mid]):
                    st = mid + 1
                else :
                    end = mid - 1
    
        return -1   