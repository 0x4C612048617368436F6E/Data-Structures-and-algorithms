from collections import Counter

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _dict = Counter(nums)
        _list = _dict.values()
        print(_list)
        for i in _list:
            if i>1:
                return True
        return False

'''
Using python collection module.
Counter returns an object denoting how many time a specific element apprears in a list
'''