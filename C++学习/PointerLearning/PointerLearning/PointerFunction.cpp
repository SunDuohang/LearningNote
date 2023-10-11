#include "PointerFunction.h"
#include <stdio.h>
using namespace std;


void testArr(void) {
	int zippo[4][2] = { {2,4}, {6,8},{1,3},{5,7} };
	int(*pz)[2];			//指向一个二维数组的指针，并且该数组的一维数组元素个数为2；
	pz = zippo;
	printf(" pz = %p,      pz + 1 = %p\n", pz, pz + 1);
	printf(" pz[0] = %p,   pz[0] + 1 = %p\n", pz[0], pz[0] + 1);
	printf(" *pz = %p,     *pz + 1 = %p\n", *pz, *pz + 1);
	printf(" zippo = %p,   zippo + 1 = %p\n", zippo, zippo + 1);
	printf(" pz[0][0] = %d,  *pz[0] = %d,  **pz = %d\n", pz[0][0], *pz[0], **pz);
	printf(" pz[2][1] = %d,  *(*(pz+2) + 1) = %d\n", pz[2][1], *(*(pz + 2) + 1));
}