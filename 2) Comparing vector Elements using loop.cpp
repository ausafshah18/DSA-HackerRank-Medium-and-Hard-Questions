/* Sparse Arrays - HackerRank Problem */
/* Issay seekha ki how to access and compare vector elements */ // arr[i] yai type use karnay kay liyai int vector below program dekh
#include <bits/stdc++.h>
using namespace std;
vector<int> matchingStrings(vector<string> strings, vector<string> queries) {
    vector<int> result; // for storing the result as a vector
    int len1 = strings.size();
    int len2 = queries.size();
    for(int i=0; i<len2; i++) //Loop 1st as described above
    {   int count =0;
        for(int j=0; j<len1; j++) //Loop 2nd as described above
        {
            if(strings[j]==queries[i])
            {
                count++; // if same increment the value of count
            }
        }
        result.push_back(count);
    }
    return result;
}