#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int num;
    int house;
    int mid = 0;
    int mid_1 = 0;
    int mid__1 = 0;
    int min = 2147483647;
    vector<int> arr;
    vector<int> ar1;

    cin >> num;

    for(int i = 0; i < num; i++){
        cin >> house;
        arr.push_back(house);
    }

    sort(arr.begin(), arr.end());

    mid = arr.at(arr.size()/2);


    cout << min << "\n";

    return 0;
}