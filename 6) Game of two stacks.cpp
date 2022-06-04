/* Game of Two Stacks */
#include <bits/stdc++.h>
using namespace std;

int twoStacks(int maxSum, vector<int> a, vector<int> b) 
{
    int sum = 0,stk1_count = 0,stk2_count = 0,moves = 0;
    // Getting elements from First Stack
    for(int i = 0;i < a.size();i++)
    {
        if(sum + a[i] > maxSum)
        {
            break;
        }
        else
        {
            sum += a[i];
            stk1_count++;
        }
    }
    moves = stk1_count;
    //Try to use elements from 2nd stack
    for(int j = 0; j< b.size();j++)
    {
        sum += b[j];
        stk2_count++;
        while(sum > maxSum && stk1_count > 0)
        {
            sum -= a[stk1_count-1]; // removing last added element from 1st stack.
            stk1_count--;
        }
        moves = (sum <= maxSum) ? max(stk1_count+stk2_count,moves) : moves;
    }
    return moves;
}

