/* Pairs (searching question) HackerRank solution */
#include<bits/stdc++.h>
using namespace std;

int pairs(int k, vector<int> arr) 
{
    int res = 0;
    set<int> myset;  // c++ stl which stores elements in sorted order and that too only one occurence
    for(int i = 0;i < arr.size();i++)
    {
        myset.insert(arr[i]);
    }
    for(int i = 0;i < arr.size();i++)
    {
        int diff = arr[i] - k;
        if(myset.count(diff))
        {
            res++;
        }
    }
    return res;
}