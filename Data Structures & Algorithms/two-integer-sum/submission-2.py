class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedSums = []
        for index, value in enumerate(nums):
            sortedSums.append([value, index])
        sortedSums.sort()
        print(sortedSums)

        slow = 0
        fast = len(sortedSums) - 1
        while slow < fast:
            current_sum = sortedSums[slow][0] + sortedSums[fast][0]

            if current_sum < target:
                slow += 1
            elif current_sum > target:
                fast -= 1
            else:
                return sorted([sortedSums[slow][1], sortedSums[fast][1]])

        return []
        