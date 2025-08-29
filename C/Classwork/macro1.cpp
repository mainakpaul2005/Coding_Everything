#include<stdio.h>
#define PI 3.14
int main()
{
	float r,area;
	printf("Enter Radius of circle : ");
	scanf("%f",&r);
	area=PI*r*r;
	printf("\nThe area of circle = %f",area);
	return 0;
}
