#include<stdio.h>

struct CricPlayers {
    char name[50];
    int score;
};


int main()
{
	
	struct CricPlayers s2 = {"Mainak",200};
	
	printf("%s\t%d\t\n", s2.name, s2.score);
	
	return 0;
}