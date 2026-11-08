#include <iostream>
using namespace std;
struct TreeNode
{
    int val;
    TreeNode *right;
    TreeNode *left;

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
class Solution
{
public:
    int sumOfLeftLeaves(TreeNode *root)
    {
        if (root == nullptr)
        {
            return 0;
        }
        int sum = 0;
        if (root->left != nullptr && root->left->left == nullptr && root->left->right == nullptr)
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
};
void freeTree(TreeNode *root)
{
    if (root == nullptr)
        return;
    freeTree(root->left);
    freeTree(root->right);
    delete root;
}

int main()
{
    TreeNode *root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);
    Solution solution;
    int result = solution.sumOfLeftLeaves(root);

    // In kết quả ra màn hình
    cout << "Tong cac nut la ben trai la: " << result << endl;

    // Giải phóng bộ nhớ đã cấp phát động
    freeTree(root);

    return 0;
}
