def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length # 현재 다리길이

    while len(bridge) != 0: # 다리길이가 0이 아니면
        time += 1
        bridge.pop(0)

        print(bridge)

        # 건너갈 트럭이 남아 있다면
        if truck_weights:
            # 현재 다리의 트럭 무게 + 다음으로 건너갈 트럭의 무게가 주어진것보다 적다면
            if sum(bridge) + truck_weights[0] <= weight:
                # 맨 앞의 트럭을 빼서 브릿지에 넣어줌
                bridge.append(truck_weights.pop(0))
                # 그게 아니라면 0을 해줌
            else:
                bridge.append(0)
    print(time)
    return time

bridge_length = 2
weight	= 10
truck_weights = [7,4,5,6]
solution(bridge_length, weight, truck_weights)