#include <iostream>
#include <vector>
#include <queue>

using namespace std;

bool visited[9];
vector<int> graph[9];

void bfs(int start){
    //큐 선언
    queue<int> q;
    //큐에 현재 노드 값을 넣는다
    q.push(start);
    //현재 노드값 방문 처리
    visited[start] = true;
    //큐가 비어있지 않는 동안 while문 돌음
    while(!q.empty()){
        //x에 큐 맨 앞의 원소 할당
        int x = q.front();
        //큐 맨 앞원소 삭제
        q.pop();
        //해당 원소 출력
        cout << x << ' ';
        //for문으로 인접 노드 탐색
        for(int i = 0; i < graph[x].size(); i++){
            //y에 인접 노드 할당
            int y = graph[x][i];
            //인접 노드 값이 방문처리 안되어있다면
            if(!visited[y]) {
                //큐에 넣고
                q.push(y);
                //해당 노드 방문 처리
                visited[y] = true;
            }
        }
    }
}





int main(void) {
    // 노드 1에 연결된 노드 정보 저장 
    graph[1].push_back(2);
    graph[1].push_back(3);
    graph[1].push_back(8);
    
    // 노드 2에 연결된 노드 정보 저장 
    graph[2].push_back(1);
    graph[2].push_back(7);
    
    // 노드 3에 연결된 노드 정보 저장 
    graph[3].push_back(1);
    graph[3].push_back(4);
    graph[3].push_back(5);
    
    // 노드 4에 연결된 노드 정보 저장 
    graph[4].push_back(3);
    graph[4].push_back(5);
    
    // 노드 5에 연결된 노드 정보 저장 
    graph[5].push_back(3);
    graph[5].push_back(4);
    
    // 노드 6에 연결된 노드 정보 저장 
    graph[6].push_back(7);
    
    // 노드 7에 연결된 노드 정보 저장 
    graph[7].push_back(2);
    graph[7].push_back(6);
    graph[7].push_back(8);
    
    // 노드 8에 연결된 노드 정보 저장 
    graph[8].push_back(1);
    graph[8].push_back(7);
    
    bfs(1);
}