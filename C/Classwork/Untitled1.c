#include<stdio.h>
int main()
{
	int a,b,e;
	double c,d;
	printf("Enter the numerator :");
	scanf("%d",&a);
	printf("Enter the denominator :");
	scanf("%d",&b);
	c=a/b;
	printf("The division of %d and %d is : %lf",a,b,c);
	return 0;
}