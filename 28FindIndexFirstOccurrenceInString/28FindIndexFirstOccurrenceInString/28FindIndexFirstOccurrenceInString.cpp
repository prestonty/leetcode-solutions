// 28FindIndexFirstOccurrenceInString.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>

using namespace std;

int solution(string, string);

int main()
{
    cout << solution("sabutsad", "sad") << endl;
}

int solution(string haystack, string needle) {
    if (needle.length() > haystack.length()) {
        return -1;
    }
    for (int i = 0; i <= haystack.length() - needle.length(); i++) {
        if (haystack[i] == needle[0] && haystack.substr(i, needle.length()).compare(needle) == 0) {
            return i;
        }
    }
    return -1;
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
