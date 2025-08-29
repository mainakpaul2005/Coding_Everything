#include<stdio.h>
#include<math.h>
int main()
{
    int n,ch;
    double sq,rt,cb,ct;
	printf("Enter a number : ");
	scanf("%d",&n);
	printf("Enter a number between 1 and 4 \n1 for square of the number \n 2 for sqaure-root of it \n 3 for cube of the number \n 4 for cube root of it \n ");
	scanf("%d",&ch);
	switch(ch)
	{
		case 1:
			sq=n*n;
			printf("Square of %d is %lf",n,sq);
			break;
		case 2:
		    rt=sqrt(n);
		    printf("Square of %d is %lf",n,rt);
		    break;
		case 3:
		    cb=n*n*n;
		    printf("The cube of %d is %lf",n,cb);
		    break;
		case 4:
		    ct=pow(n,(.333));
			printf("The cube root of %d id %lf",n,ct);    
		default:
			printf("Enter a number within the range");
			break;
	}		
}