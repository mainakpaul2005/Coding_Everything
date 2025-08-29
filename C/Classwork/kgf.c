#include<stdio.h>
int main()
{
	int a=10;
	int b=a--;
	if (a<a++)
	{
		printf("Pushpa 3");
	}
	else
	    printf("KGF 3");
	printf("%d",b);
	return 0;
}