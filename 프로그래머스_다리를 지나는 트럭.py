from collections import deque

def solution(bridge_length, weight, truck_weights):

    trucks = deque(truck_weights)
    time = 0
    init = [0] * bridge_length
    bridge = deque(init)

    while trucks:
        bridge.popleft()
        first = trucks[0]

        if sum(bridge) + first <= weight:
            out = trucks.popleft()
            bridge.append(out)
        else:
            bridge.append(0)
        time += 1

    time = time + bridge_length
    return time

bridge_length = 5
weight = 5
truck_weights = [1, 1, 1, 1, 1, 2, 2]
solution(bridge_length, weight, truck_weights)