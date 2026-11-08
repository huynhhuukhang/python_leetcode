#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode
{
    /* data */ int val;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

TreeNode *createNode(int x)
{
    TreeNode *node = (TreeNode *)malloc(sizeof(TreeNode));

    node->val = x;
    node->left = NULL;
    node->right = NULL;
    return node;
}

int sumOfLeftLeaves(TreeNode *root)
{
    if (root == NULL)
    {
        return 0;
    }
    int sum = 0;
    if (root->left != NULL && root->left->left == NULL && root->left->right == NULL)
    {
        sum += root->left->val;
    }
    else
    {
        sum += sumOfLeftLeaves(root->left);
    }
    sum += sumOfLeftLeaves(root->right);
    return sum;
}

void freeTree(TreeNode *root)
{
    if (root == NULL)
    {
        return;
    }
    freeTree(root->left);
    freeTree(root->right);
    free(root);
}

int main()
{
    // Tao cay nhi phan
    TreeNode *root = createNode(3);

    root->left = createNode(9);
    root->right = createNode(20);

    root->right->left = createNode(15);
    root->right->right = createNode(7);

    // Tinh ket qua
    int result = sumOfLeftLeaves(root);

    printf("Tong cac nut la ben trai la: %d\n", result);

    // Giai phong bo nho
    freeTree(root);

    return 0;
}
