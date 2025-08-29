#include<stdio.h>
int main()
{
   int ch;
   int a,b;
   int s,u;
   double m,d,r;
   char add='+',sub='-',mul='*',quo='/',rem='%';
   printf("\t Simple Calculator\n");
   printf("\t -----------------\n");
   printf("Options:\n");
   printf("--------\n");
   printf("1. + (Add)\n");
   printf("2. - (Subtract))\n");
   printf("3. x (Multiply)\n");
   printf("4. / (Quotient)\n");
   printf("5. %% (Remainder)\n");
   printf("Enter the first number :");
   scanf("%d",&a);
   printf("Enter the second number : ");
   scanf("%d",&b);
   printf("Press any number from 1 to 5 according to your choice : ");
   scanf("%d",&ch);
   switch (ch)
   {
   	    case 1:
   	    	s=a+b;
   	    	printf("The Sum of %d and %d is %d.",a,b,s);
   	    	break;
   	    case 2:
   	    	u=a-b;
   	    	printf("The Subtraction of %d and %d is %d.",a,b,u);
   	    	break;
   	    case 3:	
   	        m=a*b;
   	        printf("The Multiplication of %d and %d is %lf.",a,b,m);
   	        break;
   	    case 4:
   	    	d=a/b;
   	    	printf("The Quotient when %d/%d, is %lf",a,b,d);
   	    	break;
   	    case 5:
   	    	r=a%b;
   	    	printf("The Remainder when %d/%d, is %lf",a,b,r);
   	    	break;
   	    default:
   	    	printf("Don't Be Smart!! Enter 1 to 5");
   }
   return 0;	
}