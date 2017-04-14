import collections
# For a given source string and a target string, you should output the first index(from 0) of target string in source string.
class Solution:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1

        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    break
            else:  # no break
                return i
        return -1

    def anagrams(self, strs):

        if len(strs) < 2 :
            return strs
        result=[]
        visited=[False]*len(strs)
        for index1,s1 in enumerate(strs):
            hasAnagrams = False
            for index2,s2 in enumerate(strs):
                if index2 > index1 and not visited[index2] and self.isAnagrams(s1,s2):
                    result.append(s2)
                    visited[index2]=True
                    hasAnagrams = True
            if not visited[index1] and hasAnagrams:
                result.append(s1)
        return result

    def isAnagrams(self, str1, str2):
        if  sorted (str1) == sorted(str2):
                return True
        return False
    #返回两个str中最长的公共部分
    def common_long(self,str1,str2):
        mylen = 0
        for index1,item1 in enumerate(str1):
            for index2,item2 in enumerate(str2):
                temp_flag = 0
                while temp_flag < (len(str1)-index1) and temp_flag < (len(str2)-index2) and str1[index1+temp_flag] == str2[index2+temp_flag]:
                    temp_flag = temp_flag + 1
                if temp_flag>mylen:
                    mylen = temp_flag
        return  mylen
    def rotateString(self, A, offset):
        if A is None or len(A) == 0:
            return A

        offset %= len(A)
        before = A[:len(A) - offset]
        after = A[len(A) - offset:]
        # [::-1] means reverse in Python
        A = before[::-1] + after[::-1]
        A = A[::-1]

        return A

    def isPalindrome(self, s):
        if not s:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            # find left alphanumeric character
            if not s[l].isalnum():
                l += 1
                continue
            # find right alphanumeric character
            if not s[r].isalnum():
                r -= 1
                continue
            # case insensitive compare
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True





if __name__ == '__main__':
    sol = Solution()
    print sol.common_long('changjingxiu','in')

    pass
