#include <iostream>
#include <string>

using namespace std;

int main() {

    string str;
    int cnt = 0;
    int max = -214748364;
    int arr[26] = {0, };
    char save;
    cin >> str;

    for(int k = 0; k < str.size(); k++){
        str[k] = tolower(str[k]);
    }
    int len = str.size();

    for(int i = 0; i < str.size(); i++){
        arr[i] = str[i] - 'a';
    }

    cout << toupper(save) << endl;
    
    return 0;
}