#include<stdio.h>
#define PI 3.14
#define AREA(r) (PI*r*r)
int main()
{
	float x,area;
	printf("Enter Radius of circle : ");
	scanf("%f",&x);
	area=AREA(x);
	printf("\nThe area of circle = %f",area);
	return 0;
}
