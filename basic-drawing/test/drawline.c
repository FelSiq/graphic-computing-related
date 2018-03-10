#include <stdlib.h>
#include <stdio.h>
#include <matrix.h>
#include <basic-drawing.h>

enum {
	PROGNAME,
	X1,
	Y1,
	X2,
	Y2,
	ARGNUM
};

int main(int argc, char *argv[]) {
	if (argc < ARGNUM) {
		printf("usage: %s x1 y1 x2 y2\n", argv[PROGNAME]);
		exit(1);
	}

	unsigned int rownum = 30;
	unsigned int colnum = 80;
	#ifdef DEBUG
		printf("Initing matrix with dimensions (%u, %u)...\n", rownum, colnum);
	#endif
	mattype **m = mat_init(rownum, colnum, 0);
	if (m) {
		int x1 = atoi(argv[X1]), x2 = atoi(argv[X2]);
		int y1 = atoi(argv[Y1]), y2 = atoi(argv[Y2]);

		#ifdef DEBUG
			printf("Successfully inited matrix. Now started to draw line...\n");
		#endif
		line(m, x1, y1, x2, y2, 1);
		#ifdef DEBUG
			printf("Line drew. Now printing matrix...\n");
		#endif
		mat_print(m, rownum, colnum);
		#ifdef DEBUG
			printf("Freeing memory and exitting program...\n");
		#endif
		return mat_purge(m, rownum);	
	}
	return 1;
}
