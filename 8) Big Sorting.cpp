/* Big Sorting Question of HackerRank */
#include <bits/stdc++.h>

using namespace std;

bool check(string &a, string &b)
{
    if(a.length() != b.length())
    {
        return(a.length() < b.length());
    }
    return (a<b);
}
vector<string> bigSorting(vector<string> unsorted) 
{
    sort(unsorted.begin(),unsorted.end(),check);
    return unsorted;
}
