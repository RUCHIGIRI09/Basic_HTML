class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        new_pattern = {}
        new_word = {}
        for i in range(len(pattern)):
            if new_pattern.get(pattern[i], -1) != new_word.get(words[i], -1):
                return False
            else:
                
                new_pattern[pattern[i]] = new_word[words[i]] = i

        return True
    
        