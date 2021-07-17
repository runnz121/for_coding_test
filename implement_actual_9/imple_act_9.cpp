#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

int main(){

string str;
cin >> str;
int len = str.size();
vector<char> a(len);

for(int i = 0; i<len; i++){
    a.push_back(str[i]);
}

for(int j = 0; j<len; j++){
    cout << a.at(j)<< endl;
}

    
}