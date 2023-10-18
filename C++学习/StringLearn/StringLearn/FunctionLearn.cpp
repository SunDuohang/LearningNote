#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include "FunctionLearn.h"
#include <string.h>

using namespace std;

#define MSG "I am a symbolic string constant."
#define MAXLENGTH 81
#define STRLEN 15

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

void InputsOutpus(void) {
	//字符串输入需要分配空间
	//gets()函数  在C11标准中已经被废除了
	char words[STRLEN];

	puts("Enter a string plz:");

	//gets(words);  //使用gets函数会在VS2022编译过程报错

}
/// <summary>
/// 用来表示fputs、puts、printf等函数的功能。
/// </summary>
/// <param name=""></param>

void Showfgets(void) {

	char words[STRLEN];
	puts("Enter a string plz:");
	fgets(words, STRLEN, stdin);
	printf("The string: (puts and fputs):\n");
	puts(words);
	puts("Enter a string plz:");
	fputs(words, stdout);
	// 超过STRLEN的长度，fgets函数只读入STRLEN长度
	fgets(words, STRLEN, stdin);
	printf("The string: (puts and fputs):\n");
	puts(words);
	fputs(words, stdout);
}

void Show_strlen(void) {
	char msg[] = "Things should be as simple as possible,"
		" but not simpler.";		//这种声明方式比较简单
	puts(msg);
	printf("The length of string: %d.\n", strlen(msg));  // 使用strlen函数来统计字符串长度
	for (int i = 0; i < strlen(msg); i++) {
		printf("%c", msg[i]);
	}
}

void Show_strcat(void) {
	char str1[MAXLENGTH] = "Things should be as simple as possible, ";
	char str2[MAXLENGTH] = "but not simpler.";
	puts(str1);
	puts(str2);
	printf("The length of string 1: %d.\n", strlen(str1));
	printf("The length of string 2: %d.\n", strlen(str2));
	printf("address of str1: %p, address of str2: %p", str1, str2);
	strcat(str1, str2);
	puts(str1);
	printf("The length of string 1: %d.\n", strlen(str1));
	printf("address of str1: %p, address of str2: %p", str1, str2);
}

void Show_strncat(void) {
	char str1[MAXLENGTH] = "Things should be as simple as possible, ";
	char str2[MAXLENGTH] = "but not simpler.";
	puts(str1);
	puts(str2);
	printf("The length of string1 : %d.\n", strlen(str1));
	printf("The length of string2 : %d.\n", strlen(str2));
	printf("address of str1: %p,      address of str2: %p\n", str1, str2);
	printf("sizeof str1: %d\n", sizeof(str1));
	strncat(str1, str2, sizeof(str1) - strlen(str1));
	puts(str1);
	printf("The length of string1 : %d.\n", strlen(str1));
	printf("address of str1: %p, address of str2: %p\n", str1, str2);
}

void Show_strcmp(void) {
	
}