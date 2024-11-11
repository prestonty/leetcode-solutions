#include <iostream>

using namespace std;


 // Definition for singly-linked list.
 struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
 
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        int val1, val2;
        ListNode* list3 = new ListNode();
        ListNode* current1 = list1; // head of list1
        ListNode* current2 = list2; // head of list2
        ListNode* current3 = list3;
        if (current1 != nullptr || current2 != nullptr)
            while (current1->next != NULL || current2 != NULL) {
                //current1 = current1->next;
                //current2 = current2->next;
                if (current1->next != nullptr) {
                    current1 = current1->next;
                    val1 = current1->val;
                }
                else {
                    val1 = 101;
                }
                if (current2->next != nullptr) {
                    current2 = current2->next;
                    val2 = current2->val;
                }
                else {
                    val2 = 101;
                }

                if (val2 >= val1) {
                    ListNode* newNode = new struct ListNode(val1);
                    current3->next = newNode;
                }
                else {
                    ListNode* newNode = new struct ListNode(val2);
                    current3->next = newNode;
                }
            }
        return list3;
    }
};

int main() {
    Solution sol = new Solution();

}