#include <bits/stdc++.h>
using namespace std;

long long minimumCost(long long cost1, long long cost2, long long costBoth, long long n1, long long n2)
{
    long long option1 = cost1 * n1 + cost2 * n2;
    long long option2 = costBoth * max(n1, n2);
    long long c = min(n1, n2);
    long long option3 = c * costBoth;
    if (n1 > n2)
    {
        option3 += (n1 - c) * cost1;
    }
    if (n2 > n1)
    {
        option3 += (n2 - c) * cost2;
    }
    return min({option1, option2, option3});
}

int main()
{
    long long cost1, cost2, costBoth, n1, n2;
    cin >> cost1 >> cost2 >> costBoth >> n1 >> n2;
    cout << minimumCost(cost1, cost2, costBoth, n1, n2);
    return 0;
}