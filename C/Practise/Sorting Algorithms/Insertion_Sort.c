#include <stdio.h>
#include<stdlib.h>

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int* arr;
    int n, i;
    
    printf("Enter the no of elements: ");
    scanf("%d",&n);
    
    arr = (int*) malloc(n * sizeof(int));
    
    printf("Enter the elements: ");
    
    for(i = 0; i < n; i++)
    {
    	scanf("%d",&arr[i]);
	}

    insertionSort(arr, n);
    printArray(arr, n);
    return 0;
}