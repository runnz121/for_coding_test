#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int n;
    int ar1[5];
    int cnt = 0;
    for(int i = 0; i < 5; i++){
        cin >> n;
        ar1[i] = n;
    }

    int idx = 1;
    while(1){
        int cnt = 0;
        for(int i = 0; i < 5; i++){
            if(idx >= ar1[i] &&  idx % ar1[i] == 0){
                cnt++;
            }
        }
        if(cnt >= 3){
            cout << idx;
            break;
        }
        idx++;
     }
    return 0;
}