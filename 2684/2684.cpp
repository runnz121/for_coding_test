#include <iostream>
#include <string>

using namespace std;

int main(){
    string type[8] = {"TTT","TTH","THT","THH","HTT","HTH","HHT","HHH"};
    int n;
    string coincase;
    string compare;
    int res[8] = {0,};
    cin >> n;

    int j = 0;
    while(n--){
        
        cin >> coincase;
        int len = coincase.length()-2;
        while(len--){
            compare = coincase.substr(j,3);

            for(int k = 0; k < 8; k++){
                if(compare == type[k]){
                    res[k]++;
                }
            }
            j++;
        }
        for(int x = 0; x < 8; x++){
            cout << res[x] << ' ';
        }
        cout<<"\n";
    }

    return 0;
}

