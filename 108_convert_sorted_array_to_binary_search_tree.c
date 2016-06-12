#include <assert.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* sortedArrayToBST(int* nums, numsSize) {
    return sortedArrayToBSTRecursively(nums, 0, numsSize-1);
}

struct TreeNode* sortedArrayToBSTRecursively(int* nums, int low, int high) {
    struct TreeNode* node = malloc(sizeof(struct TreeNode));
    int middle = (low+high)/2;
    node->val = nums[middle];
    node->left = sortedArrayToBSTRecursively(nums, low, middle-1);
    node->right = sortedArrayToBSTRecursively(nums, middle, high+1);
    return node;
}
