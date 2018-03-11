#include <stdlib.h>
#include <stdio.h>
#include <basic-drawing.h>

void line(mattype **m, int x1, int y1, int x2, int y2, int color) {
	if (0 <= x1 && 0 <= x2  && 0 <= y1 && 0 <= y2) {
		int dy = y2 - y1;
		int dx = x2 - x1;
		float angular_coef = INF;
		if (dx)
			angular_coef = dy/dx;
		
		register int x = MIN(x1, x2);
		register int y = MIN(y1, y2);
		// We multiply the increment by 2 to remove floating point arithmetic
		register int d = 2*dy - dx;
		register int dE = 2*dy;
		register int dNE = 2*(dy - dx); 
		
		write_pixel(m, x, y, color);
		if (dx) {
			if (ABS(angular_coef) <= 1.0) {
				dE = 2*dy;
				// Write based on vertical line boundaries
				while (x < MAX(x1, x2)) {
					// If d > 0, then choose NE (dNE = dy - dx).
					// If d <= 0, then chhose E (dE = dy).
					if (d <= 0) {
						d += dE;
						++x;
					} else {
						d += dNE;
						++x;
						++y;
					}
					write_pixel(m, x, y, color);
				}
			} else {
				dE = -2*dx;
				// Write based on horizontal line boundaries
				while (y < MAX(y1, y2)) { 
					// If d > 0, then choose NE (dNE = dy - dx).
					// If d <= 0, then chhose E (dE = dy).
					if (d <= 0) {
						d += dE;
						++y;
					} else {
						d += dNE;
						++y;
						++x;
					}
					write_pixel(m, x, y, color);
				}
			} 
		} else {
			// Draw a Vertical line
			while (y < MAX(y1, y2)) {
				++y;
				write_pixel(m, x, y, color);
			}
		}	
	}
}
