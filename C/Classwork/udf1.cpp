#include<stdio.h>
int sum(int,int);
int main()
{
	int a,b,s;
	printf("Enter Two Numbers : ");
	scanf("%d %d",&a,&b);
	s=sum(a,b);
	printf("The Sum :%d ",s);
	return 0;
}
int sum(int a,int b)
{
	int s;
	s=a+b;
	return s;
}