class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_great = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                val = stack.pop()
                next_great[val] = num
            stack.append(num)
        answer = []
        for num in nums1:
            answer.append(next_great.get(num, -1))
        return answer

