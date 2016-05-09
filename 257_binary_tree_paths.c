#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

char* stringAdd(char* str, int val) {
    char temp[10];
    if(strlen(str) == 0)
        sprintf(temp, "%d", val);
    else
        sprintf(temp, "->%d", val);

    char *newStr = (char*)malloc(sizeof(char)*100);
    strcpy(newStr, str);
    strcat(newStr, temp);
    
    return newStr;
}

void traverse(struct TreeNode *node, char* str, char** paths, int* returnSize) {
    if(node->left!=NULL)
        traverse(node->left, stringAdd(str, node->val), paths, returnSize);
    if(node->right!=NULL)   
        traverse(node->right, stringAdd(str, node->val), paths, returnSize);
    if(node->left==NULL && node->right==NULL) {
        *(paths+*returnSize) = stringAdd(str, node->val);
        (*returnSize)++;
    }
}

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** binaryTreePaths(struct TreeNode* root, int* returnSize) {
    char** paths = (char **)malloc(sizeof(char *)*100);

    traverse(root, "", paths, returnSize);
    
    return NULL;
}

int main() {
    struct TreeNode *root = (struct TreeNode *)malloc(sizeof(struct TreeNode *));
    root->val = 1;

    struct TreeNode *node1_1 = (struct TreeNode *)malloc(sizeof(struct TreeNode *));
    node1_1->val = 2;
    root->left = node1_1;

    struct TreeNode *node1_2 = (struct TreeNode *)malloc(sizeof(struct TreeNode *));
    node1_2->val = 3;
    root->right = node1_2;
    node1_2->left = NULL;
    node1_2->right = NULL;

    struct TreeNode *node2_1 = (struct TreeNode *)malloc(sizeof(struct TreeNode *));
    node2_1->val = 5;
    node1_1->left = NULL;
    node1_1->right = node2_1;
    node2_1->left = NULL;
    node2_1->right = NULL;

    int returnSize = 0;
    char** paths = binaryTreePaths(root, &returnSize); 
    assert(returnSize == 2);
    assert(strcmp(paths[0], "1->2->5") == 0);
    assert(strcmp(paths[1], "1->3") == 0);
    
    return 0;
}
