class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # the amount you gain
        # the position you travel to next

        # your limited in where you can start
        # 1. can only start where gas[i] > cost[i]

        # its a trick. Since theres only ONE UNIQUE SOLN GUARANTEED, its a greedy algorithm since u dont need to find the best one, there's only 1!!!


        # add gas[i], subtract cost[i], i++ in a circular array
        if sum(gas) - sum(cost) < 0:
            return -1

        station = 0
        totalGas = 0
        for i in range(len(gas)):
            totalGas = totalGas + gas[i] - cost[i]
            if totalGas < 0:
                station = i+1 # go to the next station
                totalGas = 0 # reset the gas
        return station
        