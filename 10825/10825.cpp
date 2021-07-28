#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

struct stu{
    string name;
    int kor, eng, math;
};

bool comp(stu a, stu b){
    if(a.kor == b.kor && a.eng == b.eng && a.math == b.math) return a.name < b.name;
    if(a.kor == b.kor && a.eng == b.eng) return a.math > b.math;
    if(a.kor == b.kor) return a.eng < b.eng;
    return a.kor > b.kor;
}

int main(){
    int num;
    cin >> num;
    vector<stu> arr(num);

    for (int i = 0; i < num; i++){
        cin >> arr[i].name >> arr[i].kor >> arr[i].eng >> arr[i].math;
    }

    sort(arr.begin(), arr.end(),comp);
    
   for(int i = 0; i < num; i++){
       cout <<arr[i].name << "\n";
   }
   return 0;
}