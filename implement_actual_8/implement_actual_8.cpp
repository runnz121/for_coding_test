#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;


int main(){

    string str1;
    cin >> str1;
    int len = str1.size();
    vector<char> a(len);
    int sum;
    for(int i = 0; i < len; i++){
        if(65 <= str1[i] && str1[i] <= 90){
            a.push_back(str1[i]);
        }else{
           sum += str1[i] - '0';
        }
    }
    sort(a.begin(), a.end());
    for (int j = 0; j < a.size(); j++){
        cout << a[j];
    }
    if(sum >0){
        cout << sum;
    }
    
}