import numpy as np

def write_pdb(coords, n_iter, X, Y, Z, FILE1):

    '''

    This function is used to save obtained coordinates into the PyMol readable format PDB.
    It also writes several other interesting stuff to plain .txt files.

    FILE1 := Coordinaten File Name (Should end with .pdb)
    coords := Nx3 array of new coordinates

    '''


    #Coordinates are round to the second decimal position to faciliate saving
    round_ = 2

    #Write head for each frame12
    FILE1.write('Model {}\n'.format(n_iter)) #Start of a frame

    cryst = 'CRYST1'+ str("{:9.3f}{:9.3f}{:9.3f}".format(X*10,Y*10,Z*10)) + "  90.00  90.00  90.00 P 1           1\n"
    FILE1.write(cryst)


    #Just iterate over all coordinates and write them down line per line
    for i, coord in enumerate(coords):

        #The PDB-formate is really strict the line below is from: https://cupnet.net/pdb-format/

        #ATOM  #ID   #NAME     #RESN      #RESID          #X    #Y     #Z
        coord_str = "{:6s}{:5d} {:^4s}{:1s}{:3s} {:1s}{:4d}{:1s}   {:8.3f}{:8.3f}{:8.3f}{:6.2f}{:6.2f}          {:>2s}{:2s}\n".format('ATOM', int(i),
                                                                                                                         'PAR', ' ', 'ARG',
                                                                                                                         ' ', int(i), ' ',
                                                                                                                         np.round(coord[0], round_)*10,
                                                                                                                         np.round(coord[1], round_)*10,
                                                                                                                         np.round(coord[2], round_)*10,
                                                                                                                          1.0, 1.0, 'Ar', ' ')

        FILE1.write(coord_str) #Write coordinates

    FILE1.write('TER\nENDMDL\n') #End of a frame



