#include<stdio.h>
int main()
	{
		int n=0,i=0;
		
		double sum=0;
		char m='+';
		printf("Enter the No of terms : ");
		scanf("%d",&n);
		for(i=1;i<=n;i++)
			{
				
				sum += (double)i / (i + 1);
				printf("(%d/%d)",i,i+1);
				if(i<n)
				{
					printf("%c",m);
				}
			}
		printf(" = %lf",sum);	
		return 0;
	}