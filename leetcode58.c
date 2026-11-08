#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lengthOfLastWord(char *s)
{
    int i = strlen(s) - 1;
    int cnt = 0;
    while (i >= 0 && s[i] == ' ')
    {
        i--;
    }
    while (i >= 0 && s[i] != ' ')
    {
        cnt++;
        i--;
    }
    return cnt;
}
int main()
{
    char s[1000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0';
    printf("tong so ki tu cua tu cuoi cung la: %d\n", lengthOfLastWord(s));
    return 0;
}