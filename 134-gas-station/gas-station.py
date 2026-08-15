class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        if sum(gas) < sum(cost):
            return -1

        total_tank=0
        curr_tank=0
        starting_station=0

        for i in range(len(gas)):
            net_gain =gas[i]-cost[i]
            curr_tank+=net_gain


            if curr_tank<0:
                starting_station =i+1
                curr_tank=0

        return starting_station           
        