#include<stdio.h>

int main()
{
	
	int n, res = n % 2;
	
	printf("Enter a Number: ");
	scanf("%d",&n);
	
	switch(res)
	{
		case 0:
			printf("The number is even.");
			break;
		case 1..n:
			printf("The number is odd.");
		default:
			printf("Wrong Choice !");
	}
	
	return 0;
}