#include<stdio.h>

int main()
{
	int n, ch = n / 2;
	int c = 0;
	
	printf("Enter a number: ");
	scanf("%d",&n);
	
	for(int i = 2; i <= ch; i++)
	{
		if(n % i == 0)
			c++;
	}
	
	if(c > 1)
		printf("The number is not prime.");
	else 
		printf("The number is Prime.");
	
	return 0;
}