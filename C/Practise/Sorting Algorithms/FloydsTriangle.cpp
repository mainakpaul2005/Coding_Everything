#include<stdio.h>

int main()
{
	int i,n,j;
	
	printf("Enter the no of lines: ");
	scanf("%d",&n);
	
	for( i = 1; i <= n; i++)
	{
		for( j = 1; j <= i; j++)
		{
			printf("%d",j);
		}
		
		printf("\n");
	}
	
	return 0;
}