/* Simple Text Editor */
#include <bits/stdc++.h>
using namespace std;

int main() 
{   
    int q;
    string s = "";
    cin >> q;
    stack <string> my;
    my.push(s);
    for(int i = 0;i < q;i++)
    {
        int x;
        cin >> x;
        switch(x)
        {
            case 1:
            {
                string w;
                cin >> w;
                s.append(w);
                my.push(s);
                break;
            }
            case 2:
            {
                int k;
                cin >> k;
                int del = s.length() - k;
                s.erase(del,s.length());  // erasing is done according to index from 1 onwards
                my.push(s);
                break;
            }
            case 3:
            {
                int k;
                cin >> k;
                cout << s[k-1] << endl;
                break;
            }
            case 4:
            {
                my.pop();
                s = my.top();
                break;
            }
        }
    }
    return 0;
}
