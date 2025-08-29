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
	int n,r;
	printf("Enter a Number : ");
	scanf("%d",&n);
	r=rev(n);
	if(n==r)
	{
		printf("%d is a Palindrome Number.",n);
	}
	else
	{
		printf("%d is not a Palindrome Number.",n);
	}
	return 0;
}