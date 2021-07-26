#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool desc(int a, int b)
{ 
    //앞의 값이 더 크게 나오도록 바꿔줌(즉 참으로 만드는 조건을 만들어줌)
    return a > b; //(a < b : 오름차순) 앞이 더 큰게 참 

}

int main(void){
    int n;
    int num;

    cin >> n;
    int ar1[n];

    for(int i = 0; i < n; i++){
        cin >> num;
        ar1[i] = num;
    }

//sort(data, data+10, desc); 
    sort(ar1, ar1+n, desc);


    for(int i = 0; i < n; i++){
        cout << ar1[i] <<"\n";
    }
    return 0;
}

// #include <algorithm>
// #include <iostream>

// using namespace std;

// int main(void){

    

//     return 0;
// }