#include <stdlib.h>
#include <stdio.h>
#include <basic-drawing.h>
#include <math.h>

void line(mattype **m, int x1, int y1, int x2, int y2, int color) {
	if (0 <= x1 && 0 <= x2  && 0 <= y1 && 0 <= y2) {
		register int x = MIN(x1, x2), y = MIN(y1, y2);
		register float angular_coef = INF;
		
		if (x1 != x2)
			angular_coef = (y2 - y1)/(1.0 * (x2 - x1));
		
		int move_x = ABS(angular_coef) <= 1.0;
		
		if (move_x) {
			while (x <= MAX(x1, x2)) {
				y = (int) round(angular_coef * (x - x1) + y1);
				write_pixel(m, x, y, color);
				++x;	
			}
		} else {
			if (x1 != x2) {
				while (y <= MAX(y1, y2)) {
					x = (int) round((y - y1)/(1.0 * angular_coef) + x1);
					write_pixel(m, x, y, color);
					++y;	
				}
			} else {
				while(y <= MAX(y1, y2)) {
					write_pixel(m, x1, y, color);
					++y;
				}
			}
		}
	}
}

