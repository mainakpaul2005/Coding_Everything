#include<stdio.h>
int main()
	{
		int i,n=10;
		int sum=0;
		char s='+';
		for(i=0;i<=n;i++)
			{
				sum=i+sum;
				printf("%d",i);
				if (i<n)
				{
					printf("%c",s);
				}
			}
		printf(" = %d",sum);		
		return 0;	
	}