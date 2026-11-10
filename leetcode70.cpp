#include <bits/stdc++.h>
using namespace std;
int climbStairs(int n)
{
    if (n <= 2)
        return n;
    int ways1 = 1;
    int ways2 = 2;
    int current = 0;
    for (int i = 3; i <= n; ++i)
    {
        current = ways1 + ways2;
        ways1 = ways2;
        ways2 = current;
    }
    return current;
}

int main()
{
    int n;
    cin >> n;
    cout << climbStairs(n);
    return 0;
}