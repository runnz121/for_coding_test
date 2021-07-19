
#include <iostream>
#include <string>

using namespace std;

int main(){
while(1){
    string n;
    int flag = 0;
    cin >> n;
    if(n == "0") break;
    for(int i = 0; i<n.size()/2; i++){
        if(n[i] != n[n.size()-1-i]){
            flag = 1;
            cout << "NO" <<endl;
            break;
        }
    }
    if (flag != 1){
        cout << "YES"<<endl;
    }
}
    return 0;
}