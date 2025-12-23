// Chapter 1
#include <stdio.h>
#include <stdlib.h>

int search(int *arr, int len, int val){
    int low = 0;
    int high = len - 1;
    
    while (low <= high){
        int idx = (high + low) / 2;

        if (arr[idx] == val){
            return idx;
        }else if (arr[idx] > val){
            high = idx - 1; // to be non inclusive
        } else {
            low = idx + 1; // to be non inclusive
        }
    }
    return -1; // If element is not found
}

int main(){
    int len = 100;
    int *arr = (int *) malloc(sizeof(int) * len);
    
    for (int i = 0; i < len; i++){
        arr[i] = i;
    }

    int val = 255;
    int res = search(arr, len, val);
    
    printf("res =  %d \n", res);
    return 0;
}