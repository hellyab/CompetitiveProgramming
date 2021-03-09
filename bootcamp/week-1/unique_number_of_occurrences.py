class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency_map = {}
        for num in arr:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
                
        frequency_set = set()
        for key in frequency_map:
            if frequency_map[key] in frequency_set:
                return False
            else:
                frequency_set.add(frequency_map[key])
        return True