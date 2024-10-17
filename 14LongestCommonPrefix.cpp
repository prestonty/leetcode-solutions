#include <string>
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string answer;

        for(int i = 0; i < strs[0].length(); i++) {
                char cpr = (strs[0])[i];
            for(int j = 0; j < strs.size(); j++) {
                if(cpr != strs[j][i])
                    return answer;
            }
            answer+=cpr;
        }
        return answer;
    }
};

int main() {
    Solution runCode = new Solution();
    using namespace std;
    strs = ["flower","flow","flight"]
    cout << runCode.longestCommonPrefix(strs);
}
