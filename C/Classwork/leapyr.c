#include<stdio.h>
int main(){
	int y;
	printf("Enter a Year of your choice : ");
	scanf("%d",&y);
	if (y%400!=0){
		if (y%4==0)
		   printf("%d is a Leap Year.",y);   
		
	}
	else
	    printf("%d is not a Leap Year.",y);
	return 0;    
}

