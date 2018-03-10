#include <stdlib.h>
#include <stdio.h>
#include <draw-essentials.h>

void write_pixel(mattype **m, int x, int y, int color) {
	m[y][x] = color;
}
