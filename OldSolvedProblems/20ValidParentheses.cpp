class Solution {
public:
    bool isValid(string s) {
        stack<char> tower;
        
        for(int i = 0; i < s.length(); i++) {
            if(s[i] == '(' || s[i] == '[' || s[i] == '{') {
                tower.push(s[i]);
            } else if(!tower.empty() && (s[i]==')'&&tower.top()=='(' || s[i]==']'&&tower.top()=='[' || s[i] =='}'&&tower.top() == '{')) {
                    tower.pop();
            } else {
                return false;
            }
        }
        if(tower.empty()) {
            return true;
        }
        return false;
    }
};