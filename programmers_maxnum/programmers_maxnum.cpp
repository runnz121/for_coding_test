#include <string>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

bool compare(string i, string j){
    if(i[0] == j[0]){
        return i.length() < j.length();
    }
    else if(i[0] == j[0]){
        if(i.length() == j.length()){
            for(int k = 0; k < i.length(); k++){
                if(i[k] < j[k]){
                    return j < i;
                }
            }
        }
    }
    return j[0]< i[0];
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> str;

    for(int i = 0; i < numbers.size(); i++){
        str.push_back(to_string(numbers.at(i)));
    }
    sort(str.begin(),str.end(), compare);
    
    for(int i = 0; i < str.size(); i++){
        answer += str.at(i);
    }

    return answer;
}