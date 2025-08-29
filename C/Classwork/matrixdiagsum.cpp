#include<stdio.h>
int main()
{
	int r,c,i,j,s;
	printf("Enter Rows : ");
	scanf("%d",&r);
	printf("Enter Columns : ");
	scanf("%d",&c);
	int dia[r][c];
	printf("Enter the elements of array : \n");
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			scanf("%d",&dia[i][j]);
		}
	}
	for(i=0;i<r;i++)
	{
		printf("\n");
		for(j=0;j<c;j++)
		{
		    printf("%d\t",dia[i][j]);	
		}
	}
	for(i=0;i<r;i++)
	{
		s=s+dia[i][i];
	}
	printf("Sum of Diagonal Elements : %d",s);
	return 0;
}