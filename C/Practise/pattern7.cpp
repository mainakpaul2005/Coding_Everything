//******
//*    *
//*    *
//*    *
//*    *
//******   
// upto n lines 

#include<stdio.h>

int main()
{
	
	int n, i, j, s;
	
	printf("Enter No of Lines: ");
	scanf("%d",&n);
	
	for(i=1;i<=n;i++)
	{
		printf("*");
		
		if(i==1 || i==n)
		{
		    for(j=1;j<=n;j++)
		    {
		    	printf("*");
			}
		}
		else 
		{
			// for space printing
			
			for(s=1;s<=n;s++)
			{
				printf(" ");
			}
		}
		printf("*");
		
		printf("\n");
	}
}