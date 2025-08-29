#include<stdio.h>
#define f(x) ((x*x*x)-(3*(x*x))+(2*x)+10)

int main()
{
	int a,b,c,d,e;
	
	printf("Enter the points to check : \n");
	scanf("%d %d %d %d %d",&a,&b,&c,&d,&e);
	printf("\nThe points are : %d,%d,%d,%d,%d",a,b,c,d,e);
	
	printf("\nThe values of f(x) are : \n");
	printf(" f(%d) = %d",a,f(a));
	printf("\nf(%d) = %d",b,f(b));
	printf("\nf(%d)= %d",c,f(c));
	printf("\nf(%d)= %d",d,f(d));
	printf("\nf(%d)= %d",e,f(e));
	
}