#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int> > commands) {
    vector<int> answer;
    vector<int> dst;
    int res;

    for(int i = 0; i < commands.size(); i++){
        int begin = commands[i][0];
        int end =  commands[i][1];
        int pic = commands[i][2];

        for(int j = begin-1; j < end; j++){
            dst.push_back(array[j]);
        }
        sort(dst.begin(),dst.end());
        answer.push_back(dst[pic-1]);
        dst.clear();
    }
    return answer;
}