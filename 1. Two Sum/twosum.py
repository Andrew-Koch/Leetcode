class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        '''
       #For all elements in list try to sum to target:
        for i, x in enumerate(nums[:-1]):
            val = x
            #Find sum of elements and return indices if match:
            for j, y in enumerate(nums[i+1:]):
                if x+y == target:
                    return ([i, j+i+1])
        '''

        #List comprehension version:
        return next(([i, j+i+1] for i, x in enumerate(nums[:-1]) for j, y in enumerate(nums[i+1:]) if x+y == target))
