#include<stdio.h>
int main()
	{
		int i,j,r,c;
		int arr1[10][10];
		printf("\n Enter number number of rows :");
		scanf("%d",&r);
		printf("\n Enter number number of columns :");
		scanf("%d",&c);
		printf("\n Enter elements of matrix:");
		
		for(i=0;i<r;i++)
			{
				
				for(j=0;j<c;j++)
					{
						scanf("%d",&arr1[i][j]);
					}
			}
			
		printf("\n Entered matrix is:");	
			for(i=0;i<r;i++)
			{
				printf("\n");
				for(j=0;j<c;j++)
					{
						printf("%d\t",arr1[i][j]);
					}
			}
			
	return 0;		
	}