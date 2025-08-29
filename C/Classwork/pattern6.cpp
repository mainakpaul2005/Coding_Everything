#include<stdio.h>
int main() {
   int i, space, rows, k=1;
   printf("Enter the number of rows: ");/*number of rows taking from user*/
   scanf("%d", &rows);
   for (i = 1; i <= rows; ++i, k=1) {
   		printf("\n");
      for (space = 1; space <= rows - i; ++space) {
         printf("  ");
      }
      while (k <=i) {
         printf("%c ",64+k);
         ++k;
      }
      printf("\n");
   }
   return 0;
}