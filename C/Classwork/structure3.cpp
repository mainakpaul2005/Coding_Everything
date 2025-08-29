#include<stdio.h>
struct cricketer
{
    int runs;
    char name[15];
    char country[10];
}player[10],t;
 
int main()
{
    int i,j,n;
    printf("Enter the no of cricket players\n");
    scanf("%d",&n);
    if (n>10)
    { printf ("Number of players should not be greater than 10");
    }
    else 
    {
    printf("Enter player info as name , country , runs scored\n");
    for(i=0;i<n;i++)
    {
        scanf("%s %s %d",player[i].name,&player[i].country,&player[i].runs);
    }
    
        
    for(i=0;i<n;i++)
    {
        for(j=0;j<n-1;j++)
        {
            if(player[j].runs>player[j+1].runs)
            {
                t=player[j];
                player[j]=player[j+1];
                player[j+1]=t;
            }
        }
    }
    
    printf("\nCricketer info in ascending order of runs\n");
    printf("\nName\t\tCountry\t\tRuns scored\n");
    //printf("-------------------------------------------------------------------------------\n");
 
    for(i=0;i<n;i++)
    {
        printf("%s\t\t%s\t\t%d\n",player[i].name,player[i].country,player[i].runs);
    }}
    return 0;
}