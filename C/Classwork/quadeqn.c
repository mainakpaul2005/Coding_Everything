#include<stdio.h>
#include<math.h>
int main()
{
	printf("The general form of a Quadratic Equation :\n\n \tax**2 + bx + c = 0\n\n");
	printf("The solution can be found by using Sridhar Acharya's Method.\n\n");
	printf("where, Discriminant D = {(b**2)-4ac}\n\n");
	printf("\tIf D>0,\n The Roots are Distinct and Real.\n");
	printf("\tIf D=0,\n The Roots are Equal and Real.\n");
	printf("\tIf D<0,\n The Roots are Complex or Imagionary.\n\n");
	printf("The Roots will be :\n\n");
	printf("\tLet x1 and x2 be the two roots then,\n\n");
	printf("\t\tx1= [-b+{(b**2)-4ac}]/2a\n");
	printf("\t\tx2= [-b-{(b**2)-4ac}]/2a\n\n ");
	printf("where, b = coefficient of x\n\ta = coefficient of x**2,and\n\tc = constant term.");
	printf("\n\n");
	double b,a,c;
	printf("Enter the coefficient of x**2(a) : ");
	scanf("%lf",&a);
	printf("Enter the coefficient of x(b) : ");
	scanf("%lf",&b);
	printf("Enter the constant term(c) : ");
	scanf("%lf",&c);
	printf("%lf %lf %lf",a,b,c);
	double D,x1,x2;
	D=(pow(b,2))-(4*a*c);
	if (D>0)
	{
		printf("\n\nThe Roots of the equation are Real and Distinct.\n\n");
		x1=(-b+D)/(2*a);
		x2=(-b-D)/(2*a);
		printf("The Roots are : \n \t %lf \n\t %lf",x1,x2);
	}
	else if (D==0)
	{
	    printf("The Roots of the equation are Real and Equal.\n\n");
		x1=(-b+D)/(2*a);
		x2=(-b-D)/(2*a);
		printf("The Roots are : \n \t %lf \n\t %lf",x1,x2);	
	}
	else if (D<0)
	{
		printf("The Roots of the equation are Imaginary.\n\n");
	}
	else
	    printf("Unprecedented Error.");
}
