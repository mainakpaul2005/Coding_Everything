#include<stdio.h>
 
int main()
{
    int i, j, rows, columns,c=1;
     
    printf(" \nPlease Enter the Number of Rows : ");
    scanf("%d", &rows);
    
    printf(" \nPlease Enter the Number of Columns : ");
    scanf("%d", &columns);
     
    for(i = 1; i <= rows; i++)
    {
    	for(j = 1; j <= columns; j++)
		{
			if(i == 1 || i == rows || j == 1 || j == columns)
			{
				printf("%d",c);
				c++;
			}
			else
			{
				printf(" ");
			}       	
        }
        printf("\n");
    }
    return 0;
}
