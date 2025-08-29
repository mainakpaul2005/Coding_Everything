#include<stdio.h>
int main()
{
	int a;
	printf("Enter Your Age : ");
	scanf("%d",&a);
	(a>=18)?printf("You are eligible to vote"):printf("You are not eligible to vote");	
	return 0;
}