class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = {}

        for num in nums:
            if record.get(num) is None:
                record.update({num: 1})
            else:
                record.update({num: record[num] + 1})
        a = sorted(record.items(), key=lambda item: item[1], reverse=True)

        final = []
        for i in range(0,k):
            final.append(a[i][0])
        
        return(final)