CFLAGS = -D DEBUG -Wall -I ./libs/ -lm

all: essentials.mk matrix.mk basicdraw.mk test.mk
	gcc draw-essentials.o matrix.o vec-to-mat-bresenham-foley.o drawline.o -o ./test/drawline $(CFLAGS)
	rm *.o
essentials.mk:
	gcc -c ./essentials/draw-essentials.c $(CFLAGS)
matrix.mk:
	gcc -c ./matrix/matrix.c $(CFLAGS)
basicdraw.mk:
	gcc -c ./lines/vec-to-mat-bresenham-foley.c $(CFLAGS)
test.mk:
	gcc -c ./test/drawline.c $(CFLAGS)
