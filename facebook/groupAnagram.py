class Solution(object):
    def groupAnagrams(self, strs):
        anagram = dict()
        for string in strs:
            sortedStr = "".join(sorted(string))
            if sortedStr in anagram:
                tmp = anagram[sortedStr]
                tmp.append(string)
                anagram[sortedStr] =tmp
            else:
                anagram[sortedStr] = [string]
        
        vals = anagram.itervalues()
        res = [x for x in vals]
        
        return res