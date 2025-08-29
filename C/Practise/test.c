#include<stdio.h>
int main()
{
	int a;
	printf("Enter Your Age : ");
	scanf("%d",&a);
	if(a>=18)
	{
		printf("Hello World !");
	}
	else if(a<1)
	{
		printf("Don't be oversmart. ");
	}
	else
	{
		printf("You are not eligible.");
	}
	return 0;
}