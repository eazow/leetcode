#include <assert.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* sortedArrayToBSTRecursively(int* nums, int low, int high) {
    if(low > high) return NULL;
    struct TreeNode* node = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    int middle = (low+high)/2;
    node->val = nums[middle];
    node->left = sortedArrayToBSTRecursively(nums, low, middle-1);
    node->right = sortedArrayToBSTRecursively(nums, middle+1, high);
    return node;
}

struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    return sortedArrayToBSTRecursively(nums, 0, numsSize-1);
}

int main() {
    int nums[3] = {1,2,3};
    struct TreeNode* root = sortedArrayToBST(nums, 3);
    assert(root->val == 2);
    assert(root->left->val == 1);
    assert(root->right->val == 3);

    return 0;
}
