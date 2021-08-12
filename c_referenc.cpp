#include <bits/stdc++.h>

using namespace std;

int main(){

    std::ios_base::sync_with_stdio(false);
    //os_base: cin, cout 등
    // sync: 동기화하다
    // with stdio: stdio (printf, scanf, getchar, fgets, puts, putchar 등)와
    // false: (동기화를) 하지 않는다
    // 따라서 ios_base::sync_with_stdio(false);를 한 이후로는 cin / scanf를 같이 쓰거나 cout / printf를 같이 쓰면 문제가 발생할 수 있습니다.


    cin.tie(0);
    //cin을 cout으로부터 untie합니다. stream을 tie하면 다른 stream에서 입출력요청이 오기전에 stream을 flush시킵니다.:
    //기본적으로 cin과 cout은 묶여있고 묶여있는 스트림들은 한 스트림이 다른 스트림에서 각 IO 작업을 진행하기 전에 자동으로 버퍼를 비워줌을 보장합니다.

    
    return 0;
}