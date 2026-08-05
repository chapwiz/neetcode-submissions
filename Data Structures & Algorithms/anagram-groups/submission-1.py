class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = []
        result = []

        if len(strs) == 1:
            return [strs]

        for word in strs:
            curr = Counter(word)
            if curr not in seen:
                seen.append(curr)
                result.append([word])
            else:
                result[seen.index(curr)].append(word)
        return result
