
#include <stdio.h>
void swap(int x, int y) {
 int temp = x;
 x = y;
 y = temp;
}
int main() {
 int a = 40, b = 50;
 printf("Before swap, a = %d and b = %d\n", a, b);
 swap(a, b);
 printf("After swap, a = %d and b = %d\n", a, b);
 return 0;
}