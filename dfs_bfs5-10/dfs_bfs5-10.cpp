#include <iostream>

using namespace std;

int n,m;
int graph[1000][1000];

bool DFS(int x, int y){
    if(x <= -1 || x >= n || y <= -1 || y >= n){
        return false;
    }

    if(graph[x][y] == 0){
        graph[x][y] = 1;
        DFS(x-1, y);
        DFS(x,y-1);
        DFS(x+1,y);
        DFS(x,y+1);
        return true;
    }
    return false;
}

int main(void){
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
        //https://www.acmicpc.net/board/view/55135 cin과 scanf 차이점
        scanf("%1d", &graph[i][j]);     
        }
    }

    int res = 0;
    for (int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if (DFS(i,j)){
                res += 1;
            }
        }
    }
    cout << res << "\n";
    return 0;
}