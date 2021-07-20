#include <iostream>
#include <string>
#include <algorithm>

using namespace std;


int main() {

    string str,str1, str2;
    int nstr, nstr1, nstr2;

    cin >> str1 >> str2;

    string rstr1 (str1.rbegin(), str1.rend());
    string rstr2 (str2.rbegin(), str2.rend());

    nstr1 = stoi(rstr1);
    nstr2 = stoi(rstr2);

    nstr = nstr1 + nstr2;

    str = to_string(nstr);
    string rstr (str.rbegin(), str.rend());

    nstr = stoi(rstr);

    cout << nstr << "\n";

    return 0;
}