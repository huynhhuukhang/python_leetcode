#include <bits/stdc++.h>
using namespace std;

int uniquePaths(int m, int n)
{
    vector<int> dp(n, 1);
    for (int i = 1; i < m; ++i)
    {
        for (int j = 1; j < n; ++j)
        {
            dp[j] += dp[j - 1];
        }
    }
    return dp[n - 1];
}
int main()
{
    int n;
    cin >> n;
    int m;
    cin >> m;
    cout << uniquePaths(m, n);
    return 0;
}