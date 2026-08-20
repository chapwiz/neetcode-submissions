class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const items = new Set();

        for (let x of nums) {
            items.add(x);
        }

        if (nums.length != items.size) {
            return true
        }

        return false
    }
}
