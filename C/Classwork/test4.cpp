#include <stdio.h>
#include <math.h>
#include <stdbool.h> // For boolean data type

int main() {
    double num;
    char choice;
    bool quit = false;

    while (!quit) {
        printf("Enter a number: ");
        scanf("%lf", &num);

        if (num < 0) {
            printf("Cannot calculate square root or cube root of a negative number.\n");
        } else {
            double sqrt_num = sqrt(num);
            double cbrt_num = cbrt(num); // Use cbrt() for cube root

            printf("Square root of %.2lf is %.2lf\n", num, sqrt_num);
            printf("Cube root of %.2lf is %.2lf\n", num, cbrt_num);
        }

        // Clear the input buffer (important for preventing issues with scanf)
        while (getchar() != '\n'); //This line is crucial to clear the buffer

        printf("Do you want to continue? (y/n): ");
        scanf("%c", &choice);

        if (choice == 'n' || choice == 'N') {
            quit = true;
        }
        else if (choice == 'y' || choice == 'Y') {
            quit = false;
        }
        else{
             printf("Invalid choice. Please enter 'y' or 'n'.\n");
             quit = false; // Stay in the loop
        }
    }

    printf("Exiting program.\n");
    return 0;
}
