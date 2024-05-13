// 67AddBinary.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>

using namespace std;

string solution(string, string);

int main()
{
    cout << solution("11", "1") << endl;
}

string solution(string a, string b) {
    int biggerLength;
    if (a.length() >= b.length()) {
        biggerLength = a.length();
    }
    else {
        biggerLength = b.length();
    }
    int carryOver = 0;
    string c = "";
    int aVal;
    int bVal;
    // Yeah So I get rndom errors if I use b.length() in my calculations, idk why
    int bL = b.length();
    int aL = a.length();
    for (int i = 0; i < biggerLength; i++) {
        if (aL - 1 - i < 0) {
            a = "0" + a;
        }
        aVal = stoi(string(1,a[a.length() - 1 - i]));
        if (bL - 1 - i < 0) {
            b = "0" + b;
        }
        bVal = stoi(string(1,b[b.length() - 1 - i]));

        int sum = carryOver + aVal + bVal;
        if (sum == 0 || sum == 1) {
            carryOver = 0;
            c = to_string(sum) + c;
        }
        else if (sum == 2) {
            carryOver = 1;
            c = "0" + c;
        }
        else if (sum == 3) {
            carryOver = 1;
            c = "1" + c;
        }
    }
    if (carryOver != 0) {
        c = to_string(carryOver) + c;
    }
    return c;
}


// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
