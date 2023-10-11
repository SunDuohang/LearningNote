// PointerLearning.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include "PointerFunction.h"
using namespace std;

void test(void);
void test1(void);

int main()
{
    //test();
    //test1();
    testArr();
}

void test(void) {
    int zippo[4][2] = { {2,4},{6,8},{1,3},{5,7} };
    printf("zippo = %p,   zippo+1 = %p\n", zippo, zippo + 1);
    printf("zippo[2][1] = %d,     *(*(zippo+2) + 1) = %d,    *((*zippo+2) + 1) = %d\n", zippo[2][1], *(*(zippo+2) + 1), *((*zippo+2)+1));
    printf("*(zippo+2) = %p,    zippo+2 = %p, *(zippo+2) + 1 = %p\n", *(zippo + 2), zippo + 2, *(zippo + 2) + 1);
    //zippo 和 *zippo 虽然都指向zippo[0][0]，即存储的都是zippo[0][0]的地址，但是，其移动方式并不相同，
    //zippo 表示其是按照一个int [2]（2*4Bytes）的一维数组方式移动，*zippo则是按照一个int元素（4Bytes）的方式移动
    printf("zippo = %p,   *zippo = %p,      *(zippo+2) + 1 = %p,         (*zippo+2) + 1 = %p\n", zippo, *zippo, *(zippo + 2) + 1, (*zippo + 2) + 1);
}

void test1(void) {
    int zippo[4][2] = { {2,4},{6,8},{1,3},{5,7} };
    // 看输出，可知zipp[0] 与 *zippo 移动方式是相同的，都是按照一个int型元素移动的。
    printf("    zippo = %p,      zippo + 1 = %p\n", zippo, zippo + 1);
    printf("    zippo[0] = %p,      zippo[0] + 1 = %p\n", zippo[0], zippo[0] + 1);
    printf("    *zippo = %p,      *zippo + 1 = %p\n", *zippo, *zippo + 1);
    printf("    zippo[0][0] = %d,     *zippo[0] = %d,     **zippo = %d\n", zippo[0][0], *zippo[0], **zippo);
}

// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
