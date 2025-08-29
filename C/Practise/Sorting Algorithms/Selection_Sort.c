//selection sort 

#include <stdio.h>
#include<stdlib.h>

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

void printArray(int arr[], int n) {
	printf("The Array in Sorted Order: ");
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

    selectionSort(arr, n);
    printArray(arr, n);
    return 0;
}