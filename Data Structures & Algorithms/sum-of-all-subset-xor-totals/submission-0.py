class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        total = 0

        def get_xor_sum(digits : list[int]) :
            digit_sum = digits[0]
            for d in digits[1:] :
                digit_sum ^= d
            return digit_sum

        def backtrack(i, path):
            nonlocal total
            if i == len(nums):
                if path:
                    total += get_xor_sum(path)
                return

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            backtrack(i + 1, path)
        
        backtrack(0, [])
        return total