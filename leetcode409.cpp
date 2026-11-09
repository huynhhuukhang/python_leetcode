#include <bits/stdc++.h>
using namespace std;
int longestPalindrome(string s)
{
    unordered_map<char, int> mp;

    for (char c : s)
    {
        mp[c]++;
    }
    int cnt = 0;
    bool odd = false;

    for (auto x : mp)
    {
        cnt += (x.second / 2) * 2;

        if (x.second % 2 == 1)
        {
            odd = true;
        }
    }
    if (odd)
    {
        cnt++;
    }
    return cnt;
}
int main()
{
    string s;
    cin >> s;
    cout << "chuoi doi xung dai nhat la:" << endl;
    cout << longestPalindrome(s);
    return 0;
}
