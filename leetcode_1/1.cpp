class Solution {
public:
    bool isPalindrome(string s) {
        int len = s.length();
        vector<char> str;
        for(int i = 0; i < s.length(); i++){
            s[i] = tolower(s[i]);
        }

        for(int i = 0; i < s.length(); i++){
        if(97 <= s[i] && s[i] <= 122 || 48 <=s[i] && s[i] <= 57){
                str.push_back(s[i]);
            }
        }

        for(int i = 0; i < str.size(); i++){
            if(str.at(i) != str.at(str.size()-1-i)){
                return false;
                break;
            }
        }
        return true;
    }
};