#include <stdio.h>
#include<stdlib.h>

int main() {
    FILE *file;
    char ch;

    file = fopen("test.txt", "r");

    if (file == NULL) {
        printf("Error: Could not open file.\n");
        exit(1);
    }

    printf("File contents:\n");
    while ((ch = fgetc(file)) != EOF) {
        printf("%c", ch);
    }

    fclose(file);

    return 0;
}