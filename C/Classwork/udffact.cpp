#include<stdio.h>
int fact(int n)
{
	int i=1,fac=1;
	for(i;i<=n;i++)
	{
		fac=fac*i;
	}
	return fac;
}
int main()
{
	int a,f;
	printf("Enter a Number : ");
	scanf("%d",&a);
	f=fact(a);
	printf("The Factorial is : %d",f);
	return 0;
}