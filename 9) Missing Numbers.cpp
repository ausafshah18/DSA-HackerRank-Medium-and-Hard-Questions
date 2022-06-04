/* Missing Numbers solution in c++ */
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n,m;
    int freq[100001];  //range of brr[i] <= 10^4
    for(int i = 1; i <= 100000;i++)
    {
        freq[i] = 0;
    }
    cin >> n;
    int arr[n];
    for(int i = 0;i < n;i++)
    {
        
        cin >> arr[i];
        freq[arr[i]]++;
    }
    cin >> m;
    int brr[m];
    for(int i = 0;i < m;i++)
    {
        
         cin >> brr[i];
        freq[brr[i]]--;
    }
    for(int i = 1;i <= 10000;i++)
    {
        if(freq[i] != 0)
        {
            cout << i<< " ";
        }
    }
}