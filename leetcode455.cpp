#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int findContentChildren(vector<int> &g, vector<int> &s)
{
    sort(g.begin(), g.end());
    sort(s.begin(), s.end());
    int i = 0;
    int j = 0;
    int cnt = 0;
    while (i < g.size() && j < s.size())
    {
        if (s[j] >= g[i])
        {
            cnt++;
            i++;
            j++;
        }
        else
        {
            j++;
        }
    }
    return cnt;
}
int main()
{
    int n, m;
    cin >> n;
    cin >> m;
    vector<int> g(n);
    vector<int> s(m);
    for (int i = 0; i < n; i++)
    {
        cin >> g[i];
    }

    for (int i = 0; i < m; i++)
    {
        cin >> s[i];
    }
    cout << "sau day la dap an:" << endl;
    cout << findContentChildren(g, s);
    return 0;
}