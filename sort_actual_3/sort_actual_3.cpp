#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(void){
   int n,k;

   cin >> n;
   cin >> k;

   int ar1[n];
   int ar2[n];
   int temp;
   int sum = 0;

   for(int i = 0; i < n; i++){
       cin >> ar1[i];
   }
   for(int j = 0; j < n; j++){
       cin >> ar2[j];
   }

   sort(ar1, ar1+n);
   sort(ar2, ar2+n);

  int x = 0;
  while(k > 0){
      if(ar1[x] > ar2[n-1-x]){
        temp = ar1[x];
        ar1[x] = ar2[n-1-x];
        ar2[n-1-x] = temp;
      }
      x++;
      k--;
  }

for(int i = 0; i < n; i++){
    sum+= ar1[i];
}

cout << sum << "\n";


return 0;
}