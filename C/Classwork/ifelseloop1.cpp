#include <stdio.h>

int main() {

  // variables to store the three numbers
  int a, b, c;

  //take input from the user
  scanf("%d %d %d", &a, &b, &c);

  //if else condition to check whether the first number is greater than the second
  if (a > b) {

    //nested if else condition to check if a>c
    if (a > c) {
      //a is greatest
      printf("%d", a);
    } else {
      //c is the greatest
      printf("%d", c);
    }

  } else {

    //nested if else condition to check if b>c
    if (b > c) {
      //b is greatest
      printf("%d", b);
    } else {
      //c is the greatest
      printf("%d", c);
    }

  }

  return 0;
}
