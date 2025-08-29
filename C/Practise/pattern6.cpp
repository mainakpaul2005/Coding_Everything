// *******
//  *****
//   ***
//    *
// upto n lines 

#include<stdio.h>

int main()
{
	
	int n, i, j, s;
	
	printf("Enter No of Lines: ");
	scanf("%d",&n);
	
	for(i=1;i<=n;i++)
	{
		
		// for space printing
		
		for(s=1;s<=i-1;s++)
		{
			printf(" ");
		}
		
		//for * printing
		
		for(j=1;j<=2*(n-i)+1;j++)
		{
			printf("*");
		}
		
		printf("\n");
	}
	
	return 0;
}