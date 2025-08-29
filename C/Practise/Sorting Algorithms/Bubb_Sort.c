#include<stdio.h>
#include<stdlib.h>

void Bubb_Sort(int* arr, int s);

int main()
{
	int* arr;
	int s, i;
	
	printf("Enter the number of elements: ");
	scanf("%d",&s);
	
	arr = (int*) malloc(s * sizeof(int));
	
	printf("Enter the elements: ");
	
	for(i = 0; i < s; i++)
	{
		scanf("%d",&arr[i]);
	}
	
	Bubb_Sort(arr, s);
	
	printf("The Sorted Array: ");
	for(i = 0; i < s; i++)
	{
		printf("%d ",arr[i]);
	}
	
	free(arr);
	return 0;
}

void Bubb_Sort(int* arr, int s)
{
	int i, j, temp;
	
	for(i = 0; i < s-1; i++)
	{
		for(j = 0; j < s-i-1; j++)
		{
			if(arr[j] > arr[j+1])
			{
				temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
			}
		}
	}
}