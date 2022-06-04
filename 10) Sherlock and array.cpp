/* Sherlock and Array solution in c++ */
#include <bits/stdc++.h>

using namespace std;

string balancedSums(vector<int> arr) 
{
    int n = arr.size(),sum = 0,x = 0;
    for(int i = 0;i < n;i++)
    {
        sum += arr[i];
    }
    for(int i = 0;i < n;i++)
    {
        if(2*x == sum - arr[i])  // Main mathematical formula for this question
        {
            return "YES";
        }
        x += arr[i];
    }
    return "NO";
}