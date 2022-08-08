import out
import coords

c = coords.grid_setup(N=1000, L = 10, width = 0.5)

file1 = open('Test.pdb', 'w')

out.write_pdb(coords = c, n_iter = 0, FILE1=file1, X = 10, Y = 10, Z = 10)

file1.close()
