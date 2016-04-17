#include <assert.h>
#include <stdio.h>

int isValidSudoku(char** board, int boardRowSize, int boardColSize) {
    int row = 0, col = 0;
    
    printf("%c ", board[0][0]);
    for(row = 0; row < boardRowSize; row++) {
        int statics[10] = {0};
        for(col = 0; col < boardColSize; col++) {
            int num = board[row][col]-'0';
            printf("%c ", board[row][col]);
            if(num >= 0 && num <=9) {
                statics[num]++;
                if(statics[num] > 1)
                    return 0;
            }
        }
    }

    for(col = 0; col < boardColSize; col++) {
        int statics[10] = {0};
        for(row = 0; row < boardRowSize; row++) {
            int num = board[row][col] - '0';
            if(num >=0 && num <=9) {
                statics[num]++;
                if(statics[num] > 1)
                    return 0;
            }
        }
    }
    return 1;

    for(row = 0; row < boardRowSize; row+=3) {
        for(col = 0; col < boardColSize; col+=3) {
            int statics[10] = {0};
            for(int i = 0; i < 3; i++){
                for(int j = 0; j < 3; j++) {
                    int num = board[i][j];
                    if(num >= 0 && num <=9) {
                    statics[num]++;
                    if(statics[num] > 1)
                        return 0;
                    }
                }
            }
        }
    }
    return 1;
}

int main() {
    char board[9][9] = {
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}
    };

    isValidSudoku((char **)board, 9, 9);

    return 0;
}
