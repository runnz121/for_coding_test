#include <iostream>

using namespace std;

int main(){
    int cnt = 0;
    int num;
    cin >> num;
    for(int i = 5; i < num; i = i*5){
        cnt = cnt + num/i;
    }

    
    cout << cnt << "\n";

    return 0;
}