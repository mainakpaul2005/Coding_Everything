#include<stdio.h>

int main()
{
	int n=5;
	int arr[n];
	int i,s;
	printf("\n Enter number:");
	for(i=0;i<=n;i++)
	{
		scanf("%d",&arr[i]);
	}
	
	for(i=0;i<=n;i++)
	{
		s=s+arr[i];
	}
	printf("\n Sum:%d",s);
	return 0;
}