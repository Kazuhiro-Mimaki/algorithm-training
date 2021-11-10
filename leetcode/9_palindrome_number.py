class Solution:
    def isPalindrome(self, x: int) -> bool:
        input = list(str(x))
        output = []
        for i in range(len(input)):
            output.append(input.pop())
        return list(str(x)) == output