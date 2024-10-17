class Solution {
public:
    string convert(string s, int numRows) {
        string segments[numRows];
        int start = 0;
        int end = numRows;
        string temp;
        if(numRows == 1) {
            return s;
        } else if(numRows == 2) {
            for(int i = 0; i < s.length(); i++) {
                segments[i%2] += s.substr(i,1);
            }
            return (segments[0] + segments[1]);
        } else {
            temp = s.substr(start,end-start);
        }
        bool full = true;

        while(temp != "") {
            if(!full) {
                for(int i = 0; i < temp.length(); i++) {
                    segments[numRows-2-i] += temp.substr(i,1);
                }
                start += (numRows-2);
                end += numRows;
                full = true;
            } else if(full) {
                for(int i = 0; i < temp.length(); i++) {
                    segments[i] += temp.substr(i,1);
                }
                start += numRows;
                end += (numRows-2);
                full = false;
            }
            if(start >= s.length()) {
                break;
            }
            if(end < s.length()) {
                temp = s.substr(start,end-start);
            } else {
                temp = s.substr(start,s.length()-start);
            }
        }
        string result;
        for(int i = 0; i < numRows; i++) {
            result += segments[i];
        }
        return result;
    }
};