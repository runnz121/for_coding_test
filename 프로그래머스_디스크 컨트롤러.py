# 디스크 컨트롤러
import heapq

def solution(jobs):
    answer = 0
    # jobs의 최소힙
    jobs_heap = []
    # 시작 시간, 처음에는 -1 ~ 0 범위의 작업을 찾아야하므로 -1로 초기화
    start = -1
    # 현재 시간
    now = 0
    # 완료된 작업 수
    complited_jobs = 0
    # 작업의 수
    jobs_ea = len(jobs)
    # 모든 작업을 완료할 때 까지 실행
    while complited_jobs < jobs_ea:
        # 주어진 작업을 하나씩 접근
        for job in jobs:
            # 작업을 입력받은 시점이 시작 시간과 현재 시간의 사이인 경우
            if start < job[0] <= now:
                # jobs_heap에 push (최소힙)
                # 0번 인덱스를 기준으로 정렬되므로 0번 인덱스에 작업 처리 시간을 입력
                heapq.heappush(jobs_heap, [job[1], job[0]])
        # 최소힙에 작업이 들어와 있으면
        if jobs_heap:
            # 최소힙으로부터 최소 시간 작업 꺼내기
            min_job = heapq.heappop(jobs_heap)
            # 시작 시간에 현재 시간 입력
            start = now
            # 현재 시간에 최소 시간 작업을 처리한 시간 입력
            now += min_job[0]
            # answer에 현재 시간 - 최소 시간 작업을 입력받은 시점 입력
            answer += now - min_job[1]
            # 작업을 처리하였으므로 +1
            complited_jobs += 1
        # 최소힙에 아무것도 없어도 현재시간은 흘러야 하므로 +1
        else:
            now += 1

    return answer//jobs_ea

jobs1 = [[0, 3], [1, 9], [2, 6]]
jobs2 = [[0, 3], [1, 9], [5, 6]]
solution(jobs1)

# [0,3] [1, 12] [2, 8]