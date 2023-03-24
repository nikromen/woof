#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char *DOG_SOUNDS[6] = { "haf ", "bark ", "woof ", "haf ", "wuff ", "vrrr " };
double MAGIC_CONSTANT = 3.6;


char *strip(char *str) {
    size_t len = strlen(str);
    if (len == 0) {
        return str;
    }

    // todo
}


char *translate(char *input) {
    int count = (int) ((double) strlen(input) / MAGIC_CONSTANT);
    char *dog_words[count];
    for (int i = 0; i < count; ++i) {
        dog_words[count] = DOG_SOUNDS[rand() % 6];  // NOLINT(cert-msc30-c, cert-msc50-cpp)
    }

    dog_words[count - 1] = strip(dog_words[count - 1]);
    char *result;
    for (int i = 0; i < count; ++i) {
        // join array, don't do this
        result = dog_words[0];
    }

    return result;
}


int main(int argc, char *argv[])
{
    if (argc != 2) {
        fprintf(stderr, "Usage: $ woof \"TEXT\"");
        return EXIT_FAILURE;
    }

    printf("TODO");
    return EXIT_SUCCESS;
}
