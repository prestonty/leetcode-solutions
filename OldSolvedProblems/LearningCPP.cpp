// LearningCPP.cpp : This file contains the 'main' function. Program execution begins and ends there.
// Resources - https://github.com/jsjtzyy/LeetCode/blob/master/C%2B%2B%20cheat%20sheet%20for%20interview

#include <iostream>
#include <string>
#include <vector>
#include <sstream> // this is similar to StringBuilder in Java
#include <unordered_map>
#include <map>
#include <unordered_set>

#include <stack>
#include <queue>
//#include <priority_queue>

#define _USE_MATH_DEFINES // need this for M_PI
#include <math.h>
#include <cmath>

using namespace std;

int main()
{

	// String properties and methods
	// must use #include <string>
	char ch = 'a';
	string s = "1234";

	cout << stoi(s) + 2 << endl;
	cout << to_string(123) + " is a number" << endl;
	cout << s[3] << endl; // string is an array of characters
	cout << s.size() << " " << s.length() << endl;
	cout << string(1, ch) << endl; // this method will make a string containing a character repeated n number of times E.g. "aa" "aaaaa" "bbbb" etc.
	cout << ch + "pe" << endl; // cannot concatenate a character to a string, must convert first
	cout << string(1, ch) + "pe" << endl;
	cout << s.substr(0, 2) << endl; // substrings is a property of a full string, makes sense that its a method not function

	s.append("ABC"); // same as + operator
	cout << s << endl;

	s.erase(4); // erases substring starting at index 4 (removes "ABC" substring)
	cout << s << endl;
	s.erase(0, 1); // starts at position and erases specific substring length
	s.insert(0, "1"); // inserts
	s.replace(2,1, "ASDASD"); // parameters are position, length, and newStringValue
	cout << s << endl;
	reverse(s.begin(), s.end()); // reverses a string
	cout << s << endl;

	string s2 = s + "a";
	cout << s.compare(s2) << endl; // returns 1 if s is bigger, -1 if s2 is bigger, 0 if equal


	// Taking inputs with different data types and converting to string
	stringstream ss;
	ss << "year" << ' ' << 2017; // this takes in different inputs with different DATA TYPES (HUGE!!!)
	string inputString = ss.str(); // converts sstream to string
	cout << inputString << endl; // they are not separated by spaces or anything

	// .split function in Java
	string input = "abc,def,ghi";
	istringstream sss(input);
	string token;
	while (getline(sss, token, ',')) {
		cout << token << endl; // manipulate data individually here
	}

	// DATA STRUCTURES -------------------------- (arrays, stacks, queues, singly linked list, doubly linked list, maps/hashmaps, trees, graphs involving nodes and edges for distance algorithms

	// Arrays
	int nums[10] = {0}; // each value is 0?
	for (int i = 0; i < size(nums); i++) {
		cout << nums[i] << " ";
	}
	cout << endl;
	cout << size(nums) << endl; // this is how you get size of array in c++

	// Vectors
	// must use #include <vector>
	vector<int> v(10, 0); // initialize with size and default value (all elements 0)
	//vector<vector<int>> matrixA(5, vector<int>(10, 1)); // initializes a vector of int vectors (a matrix). 5*10 2D vector filled with 1's
	// idk how to access it plus i dont need to know it
	cout << "V " << v.size() << endl; // i forgot we use << to separate printing strings and integers
	
	//v.empty(); // checks if empty or not
	//v.push_back(5); // insert this element at end of vector
	//cout << v[v.size() - 1] << endl;
	//v.pop_back(); // delete last element
	//v.clear(); // removes all elements from vector
	//cout << v.size() << endl;

	//v.front(); // returns first element. same as v[0]
	//v.erase(v.begin() + 5); // deletes 6th element. MUST USE AN ITERATOR, USE .begin() as iterator and add. Since .begin() points to the first element, adding 5 means it points to 6th element now 
	//// .begin returns an iterator pointing to first element of a vector container.
	//v.insert(v.begin(), 5); // insertion position and value inserted at that place (can be a variable, etc).
	//v.begin(); // returns iterator pointing to first element (it points to a memory address of elements of a data structure)
	//v.end();; // returns iterator pointing to null beind last element (it points past the element
	//v.end() - 1; // this would be pointing to the last element

	for (vector<int>::iterator it = v.begin(); it != v.end(); ++it) {
		cout << *it << endl; // since iterator is pointing to memory address of element, dereferencing it will point to element's value
	}

	// skipped sorting and self-defined comparator


	// unordered_map, map, unordered_set, set
	unordered_map<string, int> umap;

	umap["Preston"] = 18;	// inserting key values into map
	// we can manipulate these values anytime
	umap["Preston"]++;
	cout << umap["Preston"] << endl;

	// hashmaps can be used like a dictionary, this is just ONE of the reasons why it is OP to
	unordered_map<string, int> Map1 = {
		{"One", 1},
		{"Two", 2},
		{"Three", 3}
	};

	// maps
	// difference between unordered_map and map is that map has keys in increasing order by default
	// map is a self balancing binary search tree (BST)

	map<string, int> treemap; // O(logN) time complexity
	// this is because it uses highly balanced binary searcah trees.
	treemap["Dog"] = 5;

	umap.erase("One");
	umap.empty(); // checks if empty (bool)
	umap.size();

	// traversing a hash map
	// MEMORIZE HOW TO DEFINE AN ITERATOR!! DONT FORGET THE ::iterator
	// this means that iterator is a child of this specifically defined unordered_map. makes sense
	for (unordered_map<string, int>::iterator iter = umap.begin(); iter != umap.end(); ++iter) {
		cout << iter->first << iter->second << endl; // traverse
	}

	// skipped sets
	// sets are containers that store unique elements in a sorted manner
	// elements cannot be changed once added to the set, they can only be inserted and deleted
	// implemented as BST (binary search trees)
	// It is not a map, it only stores 1 element, basically a unique sorted array
	unordered_set<int> Set;
	Set.insert(5);
	Set.erase(5);
	//Set.erase(iterator);
	Set.size();
	Set.empty(); // returns true or false to check if set is empty or not

	// stack, queue, deque
	stack<int> plates;
	queue<int> q;

	plates.top(); // access element at atop
	plates.push(10);
	plates.pop(); // pops removes the top element (method returns void, cannot store anywhere; not like Java)
	plates.empty(); // check if empty

	q.front(); // first element in queue
	q.pop(); // DOES NOT RETURN ELEMENT, IT REMOVES IT
	q.empty(); // check if empty;

	// Math
	int x = M_PI;
	//sqrt();
	//round();
	//pow(base, exp);

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
