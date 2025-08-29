#include<stdio.h>
#include<String.h>
int array(a);
int main()
{
	int i=1;
	char ans='y';
	int arr[100];
	while(ans=='y' || ans=='Y')
	{
	    array(arr);	
		
	}
	printf("Do You wish to continue?(Y/N)");
	scanf("%c",&ans);
	int j=sizeof(arr);
    printf("%d",j);
}
int array(a)
{
	int temp;
	for(i;i<=5;i++)
	{
		printf("Enter the number : ");
		scanf("%d",&temp);
		a[i]=temp;	
	}
}