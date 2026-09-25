class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # obtain the speeds of each, store (pos, speed) for each car
        pos_time  = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]

        # sort the times by car positions
        sorted_time_by_pos = [t for pos, t in sorted(pos_time, key=lambda x: x[0])]
        
        # maintain a monotonic decreasing stack - If larger time seen, that means car merged
        stack = []
        for t in sorted_time_by_pos:
            while stack and t >= stack[-1]: 
                stack.pop()
            stack.append(t)
        return len(stack)