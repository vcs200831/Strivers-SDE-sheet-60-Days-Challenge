class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for a in map(str.split, paths):
            for b, c in map(lambda d: d.split('('), a[1:]):
                hmap[c].append(f'{a[0]}/{b}')
        return filter(lambda d: len(d) > 1, hmap.values())