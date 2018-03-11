#include <stdlib.h>
#include <stdio.h>
#include <basic-drawing.h>



void line(mattype **m, int x1, int y1, int x2, int y2, int color) {
	if (0 <= x1 && 0 <= x2  && 0 <= y1 && 0 <= y2) {
		// Basic setup
		int dy = y2 - y1;
		int dx = x2 - x1;

		float angular_coef = INF;
		if (dx)
			angular_coef = dy/dx;
		
		register int x=x1, y=y1;
		register int d, dE, dNE;
		
		write_pixel(m, x, y, color);
		// We multiply the increment by 2 to remove floating point arithmetic
		if (dx) {
			if (ABS(angular_coef) <= 1.0) {
				d = 2*dy - dx;
				dNE = 2*(dy - dx);
				dE = 2*dy;
				// Write based on vertical line boundaries
				while (x < x2) {
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
				d = -2*dx + dy;
				dNE = 2*(dy - dx);
				dE = -2*dx;
				// Write based on horizontal line boundaries
				while (y < y2) { 
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
			while (y < y2) {
				++y;
				write_pixel(m, x, y, color);
			}
		}	
	}
}
