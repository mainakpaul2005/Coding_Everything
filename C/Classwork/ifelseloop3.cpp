#include <stdio.h>

int main() {

  // variable to store the year
  int year;
  printf("Enter a Year of your choice : ");
  //take input from the user
  scanf("%d", &year);

  //if else condition to check whether the year is divisible by 4
  if (year % 4 == 0) {

    //nested if else condition to check if year is divisible by 100
    if (year % 100 == 0) {

      //nested if else condition to check if year is divisible by 400
      if (year % 400 == 0) {
        //the year is a leap year
        printf("Leap year");
      } else {
        //the year is not a leap year
        printf("Not a leap year");
      }

    } else {
      //the year is a leap year
      printf("Leap year");
    }

  } else {

    //the year is not a leap year
    printf("Not a leap year");

  }

  return 0;
}
