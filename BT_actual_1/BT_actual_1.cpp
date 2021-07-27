#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int dduck;
int mid;
int n1, num;
int sum;
vector<int> arr;
int max_ele;

int binary(vector<int>& arr, int num, int begin, int end){
    while(begin <= end){
        mid = (begin + end)/2;
        for(int i = 0; i < arr.size(); i++){
            sum += arr[i] - mid;
        }
        if(sum > num){
            begin = mid;
            binary(arr, num, begin, end);
        }else if (sum < num){
            end = mid;
            binary(arr, num, begin, end);
        }else{
            return mid;
        }
    }
    return 0;
}


int main(void){

    int cut = 0;
    
    
    cin >> n1 >> num;

    for (int i = 0; i < n1; i++){
        int x;
        cin >> x;
        arr.push_back(x);
    }
    max_ele = *max_element(arr.begin(), arr.end());

    int res = binary(arr, num, 0, max_ele);

   cout << res;
    return 0;
}