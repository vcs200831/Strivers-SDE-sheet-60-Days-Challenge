class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        result, stack = 0, [-1]
        for b in range(len(arr)+1):
            while stack[-1]!=-1 and (b==len(arr) or arr[b] <= arr[stack[-1]]):
                idx, l, r = stack.pop(), stack[-1], b
                result = (result + (r-idx) * (idx-l) * arr[idx]) % 1000000007
            stack.append(b)
        return result