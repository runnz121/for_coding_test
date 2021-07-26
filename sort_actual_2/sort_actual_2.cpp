#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(void){

    

    int n;
    string name;
    int num;

    cin >> n;

   vector <pair<string,int> > v1;


    for(int i = 0; i < n; i++){
        cin >> name;
        cin >> num;

        v1.push_back(make_pair(name,num));
    }

    sort(v1.begin(),v1.end());
    for(int i = 0; i < v1.size(); i++){
        cout << v1[i].first << ' ';
    }


    return 0;
}