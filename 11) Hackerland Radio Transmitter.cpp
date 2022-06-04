/* Hackerland Radio Transmitter solution in c++ */
#include <bits/stdc++.h>

using namespace std;

int hackerlandRadioTransmitters(vector<int> x, int k) 
{
    int count = 0,n = x.size();
    sort(x.begin(),x.end());
    int i = 0,j;
    while(i < n)
    {
        j = i;
        while(x[j]-x[i] <= k && j < n)
        {
            j+=1;
        }
        j-=1;
        count++;
        i = j+1;
        while(x[i]-x[j] <= k && i < n)
        {
            i+=1;
        }
    }
    return count;
}

/* to understand check : https://www.youtube.com/watch?v=ALE3DHcTnBU*/