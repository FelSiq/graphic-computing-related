#ifndef __MATRIX_H__
#define __MATRIX_H__


/* Structs, defines ' stuff */
typedef char mattype;

/* Functions declaration */
mattype **mat_init(unsigned int rownum, unsigned int colnum, mattype color); /* init a empty matrix */
int mat_purge(mattype **m, unsigned int rownum); /* free all memory of a given matrix */
void mat_print(mattype **m, unsigned int rownum, unsigned int colnum); /* print m */

#endif
