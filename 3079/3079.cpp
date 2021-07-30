#include <bits/stdc++.h>

using namespace std;

int n,m;

vector<int> v;

int main(){


    long long int sum = 0;
    long long int res = 0;
    long long int maxval = 0;

    std::ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    v.resize(n); //공간 예약 + 쓰레기값 제거(null로 초기화하는거와 비슷)

    for(int i = 0; i < n; i++){
        cin >> v.at(i);
        maxval = max((long long int)v.at(i), maxval);
    }

    
    long long int min = 1;
    maxval = maxval * m;

    cout << maxval << "\n";

     while(min <= maxval){
        long long int mid = (min + maxval) /2;

        cout << mid << "\n";
        
        for(int i = 0; i < n; i++){
            sum += mid/v[i];
        }
        if (sum < m)
        {
            min = mid + 1;
        }else{
            res = mid;
            maxval = mid - 1;
        }
    }
    cout <<  res << "\n";
    return 0;
}

//2 3 4 6 8 9 => 5
//7 10 => 8