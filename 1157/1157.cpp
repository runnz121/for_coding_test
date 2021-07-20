#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {

    string str;
    int cnt = 0;
    int cnt1 = 0;
    int max = -214748364;
    int arr[26] = {0, };
    string type ="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string save;
    int idx;
    cin >> str;

    for(int k = 0; k < str.size(); k++){
        str[k] = tolower(str[k]);
    }
    int len = str.size();

    for(int i = 0; i < str.size(); i++){
        arr[str[i] - 'a']++;
    }

    max = *max_element(arr, arr+26);

    for(int j = 0; j < 26; j++){
     if(arr[j] == max){
         cnt1++;
         idx = j;
         save = type[idx];
     }
    }
    if(cnt1 > 1){
        cout << "?";
    }else if(cnt1 == 1){
        cout << save;
    }
    return 0;
}