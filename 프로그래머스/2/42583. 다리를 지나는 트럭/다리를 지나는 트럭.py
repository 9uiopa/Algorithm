from collections import deque
def solution(bridge_length, weight, truck_weights):
    waiting = deque(truck_weights)
    length = len(waiting) 
    trucks_bridge = deque()
    trucks_done = deque()
    time_on_bridge = []
    time = 0
    while len(trucks_done) < length: 
        time+= 1
        if trucks_bridge:
            time_on_bridge = [x+1 for x in time_on_bridge] 
            # 다리 -> 다리를 지난 트럭
            if time_on_bridge[0] == bridge_length:
                trucks_done.append(trucks_bridge.popleft())
                time_on_bridge.pop(0)
        next_truck = 0
        # 대기 트럭 -> 다리
        if waiting and sum(trucks_bridge) + waiting[0] <= weight :
            trucks_bridge.append(waiting.popleft())
            time_on_bridge.append(0)
    return time