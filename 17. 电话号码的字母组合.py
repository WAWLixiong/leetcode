class Solution:
    def letterCombination(self, digits):
        if not digits:
            return []

        book = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(index):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in book[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = []
        combinations = []
        backtrack(0)
        return combinations


if __name__ == '__main__':
    a = '23'
    solution = Solution()
    ret = solution.letterCombination(a)
    print(ret)
