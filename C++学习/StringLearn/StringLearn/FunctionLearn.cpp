#include <stdio.h>
#include "FunctionLearn.h"

using namespace std;

#define MSG "I am a symbolic string constant."
#define MAXLENGTH 81

void test(void) {
	char words[MAXLENGTH] = "I am a string in an array.";
	const char* pt1 = "something is pointing me.";
	puts("Here are some strings.");
	puts(MSG);
	puts(words);
	puts(pt1);
	words[8] = 'p';
	puts(words);
}

void test1(void) {
	char ar[] = MSG;
	const char* pr = MSG;
	printf("address of \"I am a symbolic string constant.\": %p \n", "I am a symbolic string constant.");
	printf("address of ar: %p \n", ar);
	printf("address of pr: %p \n", pr);
	printf("address of MSG: %p \n", MSG);
}

void test2(void) {
	const char* pr = MSG;
	while (*pr != '\0') {
		printf("%c", *pr);
		pr++;
	}
	printf("\nDone!");
}