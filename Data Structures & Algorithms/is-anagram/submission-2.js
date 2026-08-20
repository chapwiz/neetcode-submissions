class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;
        const sortedS = [...s].sort((a, b) => a.localeCompare(b)).join("");
        const sortedT = [...t].sort((a, b) => a.localeCompare(b)).join("");
        return sortedS == sortedT;
    }
}
