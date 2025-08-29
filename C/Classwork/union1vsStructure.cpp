#include <stdio.h>
#include <string.h>

struct Data{
   int i;
   float f;
   char str[20];
};

int main(){
   struct Data data;        
   printf("Memory occupied by Union Data: %d \n", sizeof(data));
   return 0;
}