//include necessary header files
#include <stdio.h>

//function to reverse a given number
int reverseNumber(int num) {
    int reversedNum = 0, remainder;
    
    //loop to extract each digit from the given number
    while (num != 0) {
        remainder = num % 10; //extract the last digit
        reversedNum = reversedNum * 10 + remainder; //add the digit to the reversed number
        num /= 10; //remove the last digit from the given number
    }
    
    return reversedNum; //return the reversed number
}

//main function
int main() {
    int num, reversedNum;
    
    //get input from user
    printf("Enter a number: ");
    scanf("%d", &num);
    
    //call the reverseNumber function and store the returned value in reversedNum variable
    reversedNum = reverseNumber(num);
    
    //print the reversed number
    printf("Reversed number: %d", reversedNum);
    
    return 0;
}