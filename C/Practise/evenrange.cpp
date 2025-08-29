#include<stdio.h>
int main()
{
	int i=1,r;
	printf("Enter a range : ");
	scanf("%d",&r);
	while(i<=r)
	{
		if(i%2==0)
		{
			printf("%d",i);
		}
		i++;
	}
	return 0;
}