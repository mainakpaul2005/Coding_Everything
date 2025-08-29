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
	int i,j,n,f;
	float sum;
	printf("Enter the No of terms : ");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		for(j=2;j<=n;j++)
		{
			
			sum=(float)sum+((float)i/(float)fact(j));
		}
	}
	printf("The Sum of Series : %.2lf",sum);
	return 0;
}