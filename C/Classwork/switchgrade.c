#include<stdio.h>
int main(){
	int mark;
	printf("Enter Marks of the Student : ");
	scanf("%d",&mark);
	switch(mark){
	    case 90 ... 100:
			printf("Your Grade is A");
			break;
		case 80 ... 89:
			printf("Your Grade is B");
			break;
		case 70 ... 79:
			printf("Your Grade is C");
			break;
		case 60 ... 69:
			printf("Your Grade is D");
			break;
		case 50 ... 59:
			printf("Your Grade is E");
			break;
		case 40 ... 49:
			printf("Your Grade is E-");
			break;
		default:
		    printf("You did not Pass !");
	}
	return 0;		    
}