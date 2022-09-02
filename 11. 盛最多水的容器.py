class Solution:

    def maxArea(self, height):
        max_v = -float('inf')

        size = len(height)
        for idx, i in enumerate(height):
            for j in range(idx + 1, size):
                max_v = max(max_v, (j - idx) * min(i, height[j]))
        return max_v

    def maxArea2(self, height):
        """每移动一次指针就是缩小一次问题规模"""
        l = 0
        r = len(height) - 1
        max_v = -float('inf')

        while l < r:
            max_v = max(max_v, (r - l) * min(height[l], height[r]))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_v


if __name__ == '__main__':
    a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    ret = solution.maxArea2(a)
    print(ret)
