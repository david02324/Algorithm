from heapq import heappush, heappop

def solution(jobs):
    # 총 작업량, 완료한 개수, 마지막 task 시작 시간, 요청-종료 시간의 총합
    amount, completed, last_start, time_sum = len(jobs), 0, -1, 0
    heap = []
    # 요청 시간 기준으로 정렬
    jobs.sort()
    
    # 첫 작업 시작 시간으로 초기화
    time = jobs[0][0]
    
    # 완료한 작업의 개수가 총 작업 개수보다 적다면
    while completed < amount:
        for requested, time_use in jobs:
            # 요청시간이 마지막 task 시작시간보다 나중이고, 현재시간보다 같거나 이르다면
            if last_start < requested <= time:
                # 소요 시간 기준으로 힙에 push
                heappush(heap,(time_use,requested))
        # 수행가능한 작업이 있다면
        if heap:
            last_start = time
            time_use, new_start = heappop(heap)
            time += time_use
            time_sum += time-new_start
            completed += 1
        # 없다면 시간 추가
        else:
            time += 1
    
    return time_sum // amount