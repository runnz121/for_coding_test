
#include <iostream>

using namespace std;
int main(){
   
   int answer = 0;
   int n;
   int cnt;
   int coin[4] ={500, 100, 50, 10};

   cin >> n;

   for (int i = 0;i  < 4; i++){
       int coins = coin[i];
       cnt += n/coins;
       n %= coins;
   }
    cout << cnt << endl;
}
