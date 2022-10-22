class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_s = defaultdict(int)
        counter_t = defaultdict(int)
        for ch in t:
            counter_t[ch] += 1
        left = 0
        valid = 0
        start = -1
        minlen = float('inf')
        for right in range(len(s)):
            # move right pointer, ch is the char that will be moved into the window
            ch = s[right]
            if ch in counter_t:
                counter_s[ch] += 1
                if counter_s[ch] == counter_t[ch]:
                    valid += 1
            
            # check if left border of the window needs to be updated
            while valid == len(counter_t):
                # update our min window
                if right - left < minlen:
                    minlen = right - left
                    start = left
                # left_ch is the char that will be removed from our window
                left_ch = s[left]
                left += 1
                # update the info in our window
                if left_ch in counter_s:
                    counter_s[left_ch] -= 1
                    if counter_s[left_ch] < counter_t[left_ch]:
                        valid -= 1
        if start == -1:
            return ""
        return s[start: start + minlen + 1]
        