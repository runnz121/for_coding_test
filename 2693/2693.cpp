#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){

    int n,m;
    vector<int> arr(10);

    cin >> n;

    for(int j = 0; j < n; j++){
        for(int i = 0; i < 10; i++){
            cin >>m;
            arr[i] = m;
        }

        sort(arr.begin(), arr.end());

        cout << arr[7] << endl;
    }


    return 0;
}


