import sys;read=sys.stdin.readline
import heapq

# https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj7662/

result=[]
for T in range(int(read())):
    visited=[False]*1_000_001
    minH,maxH=[],[]
    for i in range(int(read())):
        s=read().split()
        if s[0]=='I':
            heapq.heappush(minH,(int(s[1]),i))
            heapq.heappush(maxH,(-int(s[1]),i))

            # 해당 힙에 노드 값이 들어갔음으로 갱신
            visited[i]=True


        elif s[1]=='1':

            # 힙에 값이 있고, 이미 삭제된 노드라면 idx 값으로 check 배열에서 확인
            # (idx는 for문으로 인해 연속적으로 들어감으로) (False 처리는 해당 노드가 삭제됬었다는 의미)
            # 삭제된 모든 노드를 모두 Pop 해준다(이미 타 힙에서 삭제처리되었음으로)
            while maxH and not visited[maxH[0][1]]:
                heapq.heappop(maxH)

            # 만일 힙에 값이존재한다면 해당하는 노드를 삭제 처리 한다 (이 영역은 최대힙의 값이 삭제되는 곳임으로)
            if maxH:
                visited[maxH[0][1]]=False
                heapq.heappop(maxH)
        else:
            while minH and not visited[minH[0][1]]:
                heapq.heappop(minH)
            if minH:
                visited[minH[0][1]]=False
                heapq.heappop(minH)

    while minH and not visited[minH[0][1]]:
        heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:
        heapq.heappop(maxH)

    result.append(f'{-maxH[0][0]} {minH[0][0]}'if maxH and minH else'EMPTY')
print('\n'.join(result))