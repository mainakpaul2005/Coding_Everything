#include<stdio.h>
int rev(int n)
	{
	int r,reverse=0;
	while(n!=0)
		{
			r=n%10;
			reverse=reverse*10+r;
			n=n/10;
			}	
	return reverse;		
	}
int main()	
	{
		int number,revn;
		printf("\n Enter a number:");
		scanf("%d",&number);
		int original=number;
		revn=rev(number);
		printf("\n The origibal number:%d",original);
		printf("\n The reverse number:%d",revn);
		return 0;
	}