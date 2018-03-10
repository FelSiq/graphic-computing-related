#include <stdlib.h>
#include <stdio.h>
#include <matrix.h>

mattype **mat_init(unsigned int rownum, unsigned int colnum, mattype startval) {
	mattype **m = malloc(sizeof(mattype *) * rownum);
	for (register unsigned int i = 0; i < rownum; ++i) {
		m[i] = malloc(sizeof(mattype) * colnum);
		for (register unsigned int j = 0; j < colnum; ++j)
			m[i][j] = startval;
	}
	return m;
}

int mat_purge(mattype **m, unsigned int rownum) {
	if (m) { 
		for (register unsigned int i = rownum; i--; free(m[i]));
		free(m);
		return 1;
	}
	return 0;
}

void mat_print(mattype **m, unsigned int rownum, unsigned int colnum) {
	for (register unsigned int i = 0; i < rownum; ++i) { 
		for (register unsigned int j = 0; j < colnum; ++j)
			printf("%u", (unsigned int) m[i][j]);
		printf("\n");
	}
}
