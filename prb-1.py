#Merge 2 strings alternatively

class Solution(object):
        def mergeAlternately(self, word1, word2):
       
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        result = ""

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
            i+=1

        return result
        
