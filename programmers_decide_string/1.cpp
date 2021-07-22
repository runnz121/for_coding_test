#include <string>
#include <vector>
#include <algorithm>
using namespace std;
 
int m;
 
bool compare(string a, string b) {
    if (a.at(m) != b.at(m)){
        return a.at(m) < b.at(m);
    } 
    else return a < b;
}
 
vector<string> solution(vector<string> strings, int n) {
    vector<string> answer;
 
    m = n;
    //시작 부터 끝까지 , compare라는 커스텀 함수를 이용해서 sorting
    sort(strings.begin(), strings.end(), compare);
    answer = strings;
 
    return answer;
}

#include <iostream>
int main() {
    vector<string> strings = {"abce", "abcd", "cdx"};
    int n = 1;

    vector <string>test = solution(strings, n);
    for (int i = 0; i < test.size(); i++){
        cout << test[i] << " ";
    }
    cout << endl;
    return 0;
}