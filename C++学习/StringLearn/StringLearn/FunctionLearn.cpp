#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include "FunctionLearn.h"
#include <string.h>

using namespace std;

#define MSG "I am a symbolic string constant."
#define MAXLENGTH 81
#define STRLEN 15
#define LIM		20
#define STOP	"quit"

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
	//�ַ���������Ҫ����ռ�
	//gets()����  ��C11��׼���Ѿ����ϳ���
	char words[STRLEN];

	puts("Enter a string plz:");

	//gets(words);  //ʹ��gets��������VS2022������̱���

}
/// <summary>
/// ������ʾfputs��puts��printf�Ⱥ����Ĺ��ܡ�
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
	// ����STRLEN�ĳ��ȣ�fgets����ֻ����STRLEN����
	fgets(words, STRLEN, stdin);
	printf("The string: (puts and fputs):\n");
	puts(words);
	fputs(words, stdout);
}

void Show_strlen(void) {
	char msg[] = "Things should be as simple as possible,"
		" but not simpler.";		//����������ʽ�Ƚϼ�
	puts(msg);
	printf("The length of string: %d.\n", strlen(msg));  // ʹ��strlen������ͳ���ַ�������
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
	char input[LIM][MAXLENGTH];
	int ct = 0;
	printf("Enter up to %d lines (type quit to quit): \n", LIM);
	while (ct < LIM && s_gets(input[ct], MAXLENGTH) != NULL && strcmp(input[ct], STOP) != 0) {
		ct++;
	}
	printf("%d strings entered\n", ct);

}

char* s_gets(char *str, int size) {
	char* ret_val;
	int i = 0;

	ret_val = fgets(str, size, stdin);
	if (ret_val) {
		while (str[i] != '\n' && str[i] != '\0') 
			i++;
		if (str[i] == '\n')
			str[i] = '\0';
		else
			while (getchar() != '\n')
				continue;
	}
	return ret_val;
}

void SortString(void) {
	char input[LIM][MAXLENGTH];
	char* ptstr[LIM];		//char����ָ������
	int count = 0;
	int k = 0;
	printf("Input up to %d lines, and I will sort them.\n", LIM);
	printf("To stop, press Enter key at a line's strat.\n");
	while (count < LIM && s_gets(input[count], MAXLENGTH) != NULL && input[count][0] != '\0') {
		ptstr[count] = input[count];
		count++;
	}
	sortstring(ptstr, count);
	puts("\nHere's the sorted list:\n");
	for (k = 0; k < count; k++)
		puts(ptstr[k]);

}

void sortstring(char *strings [], int num) {
	char* temp = NULL;
	int top = 0, seek = 0;
	for (top = 0; top < num - 1; top++) {
		for (seek = top + 1; seek < num; seek++) {
			if (strcmp(strings[top], strings[seek]) > 0) {
				temp = strings[top];
				strings[top] = strings[seek];
				strings[seek] = temp;
			}
		}
	}
}