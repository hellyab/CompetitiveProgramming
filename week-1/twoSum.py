class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            if nums[i] in numMap:
                numMap[nums[i]].append(i)
            else:
                numMap[nums[i]]=[i]
                
            #attempting to finish everything in one pass
            num = nums[i]
            if target-num in numMap and target-num!=num:
                if numMap[num][0]<numMap[target-num][0]:
                    return numMap[num][0],numMap[target-num][0]
                else:
                    return numMap[target-num][0],numMap[num][0]
            elif target-num == num and len(numMap[num])>1:
                return [numMap[num][0],numMap[target-num][1]]
            