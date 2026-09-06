class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        # test = {}
        
        # word = "tea"
        # word1 = "eat"
        # counts = [0] * 26
        # defaultCount = [0] * 26

        # for letter in word:
        #     index = ord(letter) - 97
        #     counts[index] += 1

        # test.setdefault(tuple(counts), [word])
        # test.update({tuple(defaultCount): ["run"]})
        # test[tuple(counts)].append(word1)
        # print(tuple(counts))
        # print(test[tuple(counts)])

        # answer = []
        # for keys in test:
        #     answer.append(test[keys])

        # print(answer)
        # return [test[tuple(counts)]]

        answerDict = {}

        for word in strs:
            counts = [0] * 26

            for letter in word:
                index = ord(letter) - 97
                counts[index] += 1
            
            if tuple(counts) in answerDict:
                answerDict[tuple(counts)].append(word)
            else:
                answerDict.update({tuple(counts): [word]})

        answer = []
        for keys in answerDict:
            answer.append(answerDict[keys])
        
        return answer