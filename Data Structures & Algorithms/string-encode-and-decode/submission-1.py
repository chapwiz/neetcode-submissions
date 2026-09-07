class Solution:

    def encode(self, strs: List[str]) -> str:
        jointString = ''
        for word in strs:
            jointString += str(len(word)) + '#' + word
        print(jointString)
        return jointString
        
    def decode(self, s: str) -> List[str]:
        final = []
        temp = ''
        prev = 0
        counter = 0
        
        while (counter < len(s)):
            if s[counter] == '#':
                charNumber = ''

                for i in range(prev, counter):
                    charNumber += s[i]

                print(counter, int(charNumber))
                for j in range(counter+1, int(charNumber)+counter+1):
                    print(s[j])
                    temp += s[j]
                
                final.append(temp)
                counter += int(charNumber) + 1
                prev = counter
            else:
                temp = ''
                counter += 1

        print(final)
        return final