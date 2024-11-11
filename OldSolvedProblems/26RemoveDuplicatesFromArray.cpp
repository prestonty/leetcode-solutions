// 26RemoveDuplicatesFromArray.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main()
{
    std::cout << "Hello World!\n";
}

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        unordered_map<int, int> umap;
        for (int i = 0; i < nums.size(); i++) {
            // store each time you view a number in a map
            umap[nums[i]] = 0;
            // if you see a number twice, delete this current index from nums
        }
        int adjuster = 0;
        for (int i = 0; i < nums.size(); i++) {
            // store each time you view a number in a map
            umap[nums[i]]++;
            if (umap[nums[i]] >= 2) {
                umap[nums[i]]--; // lower its count back to 1 after removing
                nums.erase(nums.begin() + i);
                i--; // since u removed an element, need to account for change in index
                // adjuster++;
            }
            // if you see a number twice, delete this current index from nums
        }
        return nums.size();
    }
};
