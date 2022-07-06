class Solution:
    def helper(self,nums,l,r,temp):
        if l>r:
            return
        mid=(l+r)//2
        temp.append(nums[mid])
        self.helper(nums,l,mid-1,temp)
        self.helper(nums,mid+1,r,temp)
        return temp
    def sortedArrayToBST(self, nums):
        # code here
        l=0
        r=len(nums)-1
        root=self.helper(nums,l,r,[])
        return root
    


#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.sortedArrayToBST(nums)
		for _ in ans:
			print(_, end = " ")
		print()

# } Driver Code Ends