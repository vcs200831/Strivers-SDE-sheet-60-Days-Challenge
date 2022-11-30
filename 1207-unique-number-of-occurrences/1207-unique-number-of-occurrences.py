class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = {} # store index and counter as key value pair
        for i in arr:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        return len(hmap) == len(set(hmap.values()))
      