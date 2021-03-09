from collections import deque
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        frequency_stack = deque()
        for char in s:
            if len(frequency_stack) > 0:
                if len(frequency_stack) > 0 and frequency_stack[-1][0] == char:
                    temp=(char, frequency_stack[-1][1]+1)
                    frequency_stack.pop()
                    frequency_stack.append(temp)
                else:
                    frequency_stack.append((char, 1))
                if frequency_stack[-1][1] == k:
                    frequency_stack.pop()
            else:
                frequency_stack.append((char, 1))
        final_string = ''
        for item in frequency_stack:
            final_string += item[0]*item[1]
        return final_string
#brute-force approach
#
#     def removeDuplicates(self, s: str, k: int) -> str:
#         current_total  = 0
#         iterator = 0
#         same_group = self.allItemsAreTheSame(s[iterator: iterator+k])
#         while len(s) > k and iterator+(k-1) < len(s):
#             if same_group:
#                 s = s[:iterator] + s[iterator+k:]
#                 iterator = max(iterator-(k-1), 0)
#             else:
#                 iterator += 1     
#         return s
                
#     def allItemsAreTheSame(self, the_list):
#         val  = the_list[0]
#         for i in range(len(the_list)):
#             if the_list[i] != val:
#                 return False
#         return True