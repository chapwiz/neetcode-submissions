class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = {}

        for num in nums:
            if record.get(num) is None:
                record.update({num: 1})
            else:
                record.update({num: record[num] + 1})
        sortedRecord = sorted(record.items(), key=lambda item: item[1], reverse=True)

        return [item[0] for item in sortedRecord][0:k]