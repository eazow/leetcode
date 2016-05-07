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
    printf("stringAdd: %s %d\n", str, val);
    char temp[10];
    if(strlen(str) == 0)
        sprintf(temp, "%d", val);
    else
        sprintf(temp, "->%d", val);

    char *newStr = (char*)malloc(sizeof(char)*100);
    strcpy(newStr, str);
    strcat(newStr, temp);
    printf("%s\n", newStr);
    
    puts("out stringAdd");
    return newStr;
}

void traverse(struct TreeNode *node, char *str) {
    printf("traverse: %d\n", node->val);
    if(node->left)
        traverse(node->left, stringAdd(str, node->val));
    if(node->right)   
        traverse(node->right, stringAdd(str, node->val));
    if(node->left==NULL && node->right==NULL)
        printf("%s\n", stringAdd(str, node->val));
}

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** binaryTreePaths(struct TreeNode* root, int* returnSize) {
    traverse(root, "");
    
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

    struct TreeNode *node2_1 = (struct TreeNode *)calloc(1, sizeof(struct TreeNode *));
    node2_1->val = 5;
    node2_1->left = NULL;
    node2_1->right = NULL;
    node1_1->left = NULL;
    node1_1->right = node2_1;

    int returnSize = 0;
    binaryTreePaths(root, &returnSize); 

    return 0;
}
