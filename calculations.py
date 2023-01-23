import numpy as np


def transform(tMatrix,XMIN,XMAX,YMIN,YMAX):

    coords = [[],[]]

    for x in range(XMIN,XMAX):
        for y in range(YMIN,YMAX):
            coords[0].append((x))
            coords[1].append(y)



    tCoords = np.dot(tMatrix,coords)

    coordMappings = {}
    for i in range(len(tCoords[0])):
        coordMappings[coords[0][i],coords[1][i]] =tCoords[0][i],tCoords[1][i]

    return coordMappings

