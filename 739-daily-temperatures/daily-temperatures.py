class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n=len(temperatures)
        answer=[0]*n
        stack=[]
        for i,  temp in enumerate(temperatures):
            while stack and temp>temperatures[stack[-1]]:
                prev_index=stack.pop()
                answer[prev_index]=i-prev_index
            stack.append(i)
        return answer    


        