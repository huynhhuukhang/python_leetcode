#include <stdio.h>
#include <stdlib.h>

void moveZeroes(int *nums, int numsSize)
{
    int j = 0;
    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] != 0)
        {
            nums[j] = nums[i];
            j++;
        }
    }

    for (int i = j; i < numsSize; i++)
    {
        nums[i] = 0;
    }
}
int main()
{
    int nums[] = {0, 1, 0, 13, 2};
    int numSize = sizeof(nums) / sizeof(nums[0]);
    moveZeroes(nums, numSize);
    printf("Mang sau khi da di chuyen so 0:");
    for (int i = 0; i < numSize; i++)
    {
        printf("%d ", nums[i]);
    }
    printf("\n");
    return 0;
}