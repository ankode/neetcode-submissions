class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mStack = []
        answer = [0] * len(temperatures)
        for i,v in enumerate(temperatures):
            pos = 0
            while mStack and v > temperatures[mStack[-1]]:
                pos = mStack.pop()
                answer[pos] = i-pos

            mStack.append(i)
        return answer


                    
