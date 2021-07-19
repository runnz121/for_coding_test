#include <iostream>

using namespace std;
int main(){

int n,m;
long long int a,b;
cin >> n >> m;



if(m == 0){
    a = 0;
    b = n;
}else {
    a = n/m;
    b = n%m;
}

cout << a << "\n";
cout << b << "\n";

return 0;
}