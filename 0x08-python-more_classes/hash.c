#include <stdio.h>
#include <stdlib.h>

#define CAPACITY 50000 // Size of the Hash Table

unsigned long hash_function(char* str);
int main(void)
{
	char *str = "adetola";
	unsigned long index = hash_function(str);

	printf("%lu\n", index);
}


unsigned long hash_function(char* str) {
	unsigned long i = 0;
	for (int j=0; str[j]; j++)
		i += str[j];
	printf("index: %lu\n", i);
	return (i % CAPACITY);
}