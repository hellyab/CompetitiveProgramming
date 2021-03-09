from collections import deque
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        current_items = deque()
        max_substring_len = 0
        i = 0
        while i < len(t):
            difference = abs(ord(t[i])-ord(s[i]))
            if maxCost >= difference:
                maxCost -= difference
                current_items.append(difference)
                max_substring_len = max(max_substring_len, len(current_items))
                
            elif len(current_items) > 0 :
                maxCost += current_items.popleft()
                i -= 1
            i += 1
        return max_substring_len