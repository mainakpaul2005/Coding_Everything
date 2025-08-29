#include <stdio.h>

struct book{
   char title[10];
   char author[20];
   double price;
   int pages;
};

int main(){
   struct book book1 = {"Learn C", "Dennis Ritchie", 675.50, 325};
   
   printf("Title:  %s \n", book1.title);
   printf("Author: %s \n", book1.author);
   printf("Price:  %lf\n", book1.price);
   printf("Pages:  %d \n", book1.pages);
   printf("Size of book struct: %d", sizeof(struct book));
   return 0;
}