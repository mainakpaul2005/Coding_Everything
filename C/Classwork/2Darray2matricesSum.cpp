#include<stdio.h>
int main()
	{
		int i,j,r,c;
		int arr1[10][10],arr2[10][10],sum[10][10];
		printf("\n Enter number number of rows :");
		scanf("%d",&r);
		printf("\n Enter number number of columns :");
		scanf("%d",&c);
		printf("\n Enter elements of matrix1:");
		
		for(i=0;i<r;i++)
			{
				
				for(j=0;j<c;j++)
					{
						scanf("%d",&arr1[i][j]);
					}
			}
			printf("\n Enter elements of matrix2:");
		
		for(i=0;i<r;i++)
			{
				
				for(j=0;j<c;j++)
					{
						scanf("%d",&arr2[i][j]);
					}
			}
			
		
		for(i=0;i<r;i++)
			{
				
				for(j=0;j<c;j++)
					{
					sum[i][j]=arr1[i][j]+arr2[i][j];
					}
			}
			
		printf("\n Entered matrix1 is:");	
			for(i=0;i<r;i++)
			{
				printf("\n");
				for(j=0;j<c;j++)
					{
						printf("%d\t",arr1[i][j]);
					}
			}
			printf("\n Entered matrix2 is:");	
			for(i=0;i<r;i++)
			{
				printf("\n");
				for(j=0;j<c;j++)
					{
						printf("%d\t",arr2[i][j]);
					}
			}
			printf("\n Sum of two matrices is:");	
			for(i=0;i<r;i++)
			{
				printf("\n");
				for(j=0;j<c;j++)
					{
						printf("%d\t",sum[i][j]);
					}
			}
			
	return 0;		
	}