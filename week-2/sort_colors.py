class Solution:
    def sortColors(self, nums: List[int]) -> None:
        two = len(nums) - 1
        iterator = 0
        zero = 0
        
        while two >= iterator:
            if nums[iterator] == 0:
                nums[iterator], nums[zero] = nums[zero], nums[iterator]
                zero += 1
                iterator = max(iterator,zero)
            elif nums[iterator] == 2:
                nums[two], nums[iterator] = nums[iterator], nums[two]
                two -= 1
            else:                
                iterator += 1
        
        
            
        
        