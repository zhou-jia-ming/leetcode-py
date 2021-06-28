from collections import defaultdict, deque
from typing import *

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        my_dict = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                my_dict[stop].add(i)

        routes = [set(x) for x in routes]  # list->set加速查询

        q = deque([(source, 0)])
        visited_bus = set()
        visited_stops = {source}
        # BFS for stop -> bus -> stop
        while q:
            pos, step = q.popleft()
            if pos == target:
                return step
            # for all not visited bus
            for bus in my_dict[pos] - visited_bus:
                # for all not visited stop.
                for stop in routes[bus] - visited_stops:
                    visited_bus.add(bus)
                    visited_stops.add(stop)
                    q.append((stop, step + 1))
        return -1

s = Solution()
print(s.numBusesToDestination( [[1,2,7],[3,6,7]], 1, 6))
print(s.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))