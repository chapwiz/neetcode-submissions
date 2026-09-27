class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        pref = [0] * numsLength
        pref[0] = 1
        suff = [0] * numsLength
        suff[numsLength-1] = 1
        res = [0] * numsLength

        for i in range(1,numsLength):
            pref[i] = pref[i-1] * nums[i-1]
        for i in range(numsLength,1,-1):
            suff[i-2] = suff[i-1] * nums[i-1]
        for i in range(numsLength):
            res[i] = pref[i] * suff[i]

        return res