#include <stdio.h>
#include <stdlib.h>

int linear_srch(int s, int f, int* arr);

int main() {
    int* arr;
    int i, s, f, result;

    printf("Enter the number of elements: ");
    scanf("%d", &s);

    arr = (int*) malloc(s * sizeof(int));

    if (arr == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    printf("Enter the elements: \n");
    for (i = 0; i < s; i++) 
	{
        scanf("%d", &arr[i]);
    }

    printf("Enter the element to be searched: ");
    scanf("%d", &f);

    result = linear_srch(s, f, arr);

    if (result != -1)
        printf("Element found at index %d.\n", result);
    else
        printf("Element Not Found.\n");

    free(arr);
    return 0;
}

int linear_srch(int s, int f, int* arr) {
    for (int i = 0; i < s; i++) {
        if (arr[i] == f)
            return i;
    }
    return -1; // Element not found
}