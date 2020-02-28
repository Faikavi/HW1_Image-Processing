from readPgm import read_pgm, list_to_2D_list, copy
from etc_function import createHistogram
# from etc_function import createHistogram
filename = "./image/SanFranPeak_blue.pgm"
converted_img = []
matrix_img = []
col = 0
row = 0

converted_img, col, row = read_pgm(filename, col, row)
matrix_img = list_to_2D_list(converted_img, matrix_img, col, row)

print(matrix_img)