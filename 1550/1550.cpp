#include <iostream>
#include <string.h>

using namespace std;

int main(){
    string n;
    int num = 0;
    cin >> n;

    for(int i = 0; i < n.length(); i++){
        num *= 16;
      if('A'<=n[i] && n[i] <= 'F'){
        num += n[i] - 'A' + 10;
      }else{
        num += n[i]-'0';
      }
    }

  cout << num <<endl;


    return 0;
}
